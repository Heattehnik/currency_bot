import requests
from celery import shared_task

from currency.utils import parse_xml, process_parsed_info


@shared_task
def process_cbr_request():
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            xml_content = response.content
            parsed_xml = parse_xml(xml_content)
            process_parsed_info(parsed_xml)
            return f"Курс валюты обновлён"
        else:
            return f"Ошибка при получении данных. Код ответа: {response.status_code}"
    except Exception as e:
        return f"Ошибка запроса: {str(e)}"
