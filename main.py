import csv

from bs4 import BeautifulSoup

import requests


# главная функция
def parser(url: str):
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, 'lxml')

    products = soup.find_all('div', class_='product-card')

    # перебираем каждую карточку товара и собираем данные
    for product in products:
        name = product.get('data-product-name')
        print(name)

        sku = product.get('data-product-sku')
        print(sku)

        price = product.find('span', itemprop='price').get_text()
        print(price)

        find_href = product.find('meta', itemprop='name')
        href = find_href.findNext().get('href')
        print(href, '\n')


def create_csv():
    pass


def write_scv():
    pass


if __name__ == '__main__':
    parser(url='https://glavsnab.net/santehnika/rakoviny-i-komplektuyushchiye/rakoviny.html?limit=100')
