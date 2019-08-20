from bs4 import BeautifulSoup
from decimal import Decimal
from requests import request
from currency import convert


class Request:
    @staticmethod
    def get(host, params):
        return request('GET', f'{host}?date_req={params["date_req"]}')


test_cases = (
    (10 ** 3, 'EUR', 'USD', "26/02/2017", '1051.8006'),
    (10 ** 3, 'RUR', 'USD', "26/01/2016", '12.8540'),
    (10 ** 3, 'USD', 'RUR', "02/02/2017", '60309.9000'),
    (10 ** 3, 'USD', 'EUR', "10/03/2018", '805.3478'),
    (10 ** 4, 'RUR', 'USD', "07/04/2018", '172.9111'),
    (10 ** 3, 'KZT', 'XDR', "02/12/2016", '2.1745'),
    (10 ** 6, 'CHF', 'USD', "15/10/2017", '1025220.5847'),
    (10 ** 6, 'RUR', 'JPY', "26/11/2018", '1718611.7055'),
)
for amount, cur_from, cur_to, date, expected in test_cases:
    assert str(convert(amount, cur_from, cur_to, date, Request)) == expected, \
        f'Fail. Test cases - {amount}, {cur_from}, {cur_to}, {date}, {expected}'

print('All tests - Ok!')