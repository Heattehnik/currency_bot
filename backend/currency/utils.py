import xml.etree.ElementTree as ET

from currency.models import Currency


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
        currency_date = reversed(currency_date)
        print(currency_date)
        currency_date = "-".join(currency_date)
        print(f"{currency_date} получили дату")
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

