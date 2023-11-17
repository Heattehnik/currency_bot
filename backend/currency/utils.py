import xml.etree.ElementTree as ET

from currency.models import Currency


def parse_xml(xml_content):
    try:
        root = ET.fromstring(xml_content)
        currency_date = root.attrib.get('Date', '')
        currency_date = currency_date.split(".")
        currency_date = reversed(currency_date)
        currency_date = "-".join(currency_date)
        valute = root.find("./Valute[@ID='R01235']")
        char_code = valute.find('CharCode').text
        name = valute.find('Name').text
        value = valute.find('Value').text
        valute_info = {
            'code': char_code,
            'name': name,
            'rate': float(value.replace(",", ".")),
            'date': currency_date
        }
        return valute_info
    except ET.ParseError as e:
        return f"Ошибка при парсинге XML: {str(e)}"


def process_parsed_info(parsed_info):
    try:
        currency = Currency.objects.create(**parsed_info)
        return currency
    except Exception as e:
        return f"Ошибка при создании объекта Currency: {str(e)}"

