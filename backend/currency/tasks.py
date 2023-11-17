from decimal import Decimal

import requests
from celery import shared_task
import xml.etree.ElementTree as ET

from currency.models import Currency


@shared_task
def process_cbr_request():
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'

    try:
        print("Мы внутри функции")
        # Отправляем GET-запрос к указанному URL
        response = requests.get(url)
        print("после запроса")
        if response.status_code == 200:
            print("удачный запрос")
            # Если запрос успешен, парсим XML
            xml_content = response.content
            parsed_xml = parse_xml(xml_content)
            process_parsed_info(parsed_xml)
            print("Заебись!")
        else:
            print(f"С запросом борода {response.status_code}")
            return f"Ошибка при получении данных. Код ответа: {response.status_code}"
    except Exception as e:
        print(str(e))
        return f"Ошибка запроса: {str(e)}"


def parse_xml(xml_content):
    try:
        print("Парсим...")
        root = ET.fromstring(xml_content)

        valute_info = {}
        # Получаем дату из атрибута Date в элементе ValCurs
        currency_date = root.attrib.get('Date', '')
        print(f"{type(currency_date)} дата")
        currency_date = currency_date.split(".")
        print(f"{type(currency_date)} - {currency_date}")
        currency_date = currency_date.reverse()
        print(currency_date)
        currency_date = "-".join(currency_date)
        print("получили дату")
        for valute in root.findall("./Valute[@ID='R01235']"):
            char_code = valute.find('CharCode').text
            name = valute.find('Name').text
            value = valute.find('Value').text

            # Добавляем информацию о валюте в словарь
            valute_info = {
                'code': char_code,
                'name': name,
                'rate': float(value.replace(",", ".")),
                'date': currency_date  # Добавляем дату в словарь
            }
            # Можно вернуть информацию о Valute ID="R01235" как словарь
            print(type(value))
            return valute_info
    except ET.ParseError as e:
        print(f"Ошибка при парсинге {str(e)}")
        return f"Ошибка при парсинге XML: {str(e)}"


def process_parsed_info(parsed_info):
    try:
        print("Сохраняем...")
        currency = Currency.objects.create(**parsed_info)

        return currency
    except Exception as e:
        print(f"Ошибка при сохранении {str(e)}")
        return f"Ошибка при создании объекта Currency: {str(e)}"

