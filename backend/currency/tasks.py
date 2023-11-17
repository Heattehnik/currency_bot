import requests
from celery import shared_task

from currency.utils import parse_xml, process_parsed_info


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
