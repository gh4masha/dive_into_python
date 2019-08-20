import requests
from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    # response = requests.get()  # Использовать переданный requests
    params = {
        'date_req': date
    }
    # print('date', date)
    # print(params)
    # response = requests.get()
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp', params)

    # print(response.content)
    soup = BeautifulSoup(response.content, "xml")
    amount = str(amount).replace(',', '.')
    if cur_from == 'RUR':
        amount_rur = Decimal(amount)
    else:
        cur_from_in_rur = soup.find('CharCode', text=cur_from).find_next_sibling('Value').string
        cur_from_nominal = soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string

        amount_rur = Decimal(amount) * Decimal(cur_from_in_rur.replace(',', '.')) / Decimal(cur_from_nominal)
        # print(amount_rur)

    if cur_to == 'RUR':
        result = amount_rur
    else:
        cur_to_in_rur = soup.find('CharCode', text=cur_to).find_next_sibling('Value').string
        cur_to_nominal = soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string

        result = Decimal(amount_rur / Decimal(cur_to_in_rur.replace(',', '.')) * Decimal(cur_to_nominal)).quantize(
        Decimal('.0001'))

    return result  # не забыть про округление до 4х знаков после запятой

# print(convert(100, 'EUR','USD', '17/08/2019'))
