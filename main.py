import csv

from bs4 import BeautifulSoup

from model import Product

import requests


# главная функция
def parser(url: str, max_items: int):
    create_csv()

    page = 1
    count_items = 0

    # цикл переключает страницы послее каждой итерации
    while count_items < max_items:
        list_products = []
        res = requests.get(url=f'{url}&p={page}')
        soup = BeautifulSoup(res.text, 'lxml')

        products = soup.find_all('div', class_='product-card')

        # перебираем каждую карточку товара и собираем данные
        # цикл лимита карточек
        for product in products:
            if count_items >= max_items:
                break
            name = product.get('data-product-name')
            sku = product.get('data-product-sku')
            price = product.find('span', itemprop='price').get_text()
            find_href = product.find('meta', itemprop='name')
            href = find_href.findNext().get('href')
            count_items += 1
            print(f'Сейчас на {count_items}стр')

            # записываем данные в list_products
            list_products.append(Product(sku=sku, name=name, price=price, href=href))

        write_scv(list_products)
        page += 1


# создает csv файл
def create_csv():
    with open('glasvsnab.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['sku', 'name', 'price', 'href'])


# записывает данные в csv файл
def write_scv(products: list[Product]):
    with open('glasvsnab.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([product.sku, product.name, product.price, product.href])


if __name__ == '__main__':
    parser(url='https://glavsnab.net/santehnika/rakoviny-i-komplektuyushchiye/rakoviny.html?limit=100', max_items=847)
