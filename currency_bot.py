import requests
from bs4 import BeautifulSoup

usd_rub = 'https://www.google.com/search?q=курс+доллар+рубль'
gel_rub = 'https://www.google.com/search?q=курс+лари+рубль'
usd_gel = 'https://www.google.com/search?q=курс+доллар+лари'


def get_currency(url_cur):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/100.0.4896.127 Safari/537.36'}
    resp_usd_rub = requests.get(url_cur, headers=headers)
    soup = BeautifulSoup(resp_usd_rub.content, 'html.parser')
    conv_page = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
    result_usd_rub = conv_page[0].text
    return result_usd_rub


def send_currency():
    result_usd_rub = ('Exchange rate now:\n'
                      'USD\RUB: {}₽\n'
                      'GEL\RUB: {}₽\n'
                      'USD\GEL: {}₾'.format(get_currency(usd_rub),
                                            get_currency(gel_rub),
                                            get_currency(usd_gel)))
    return result_usd_rub

