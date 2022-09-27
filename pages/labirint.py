#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='search-field')

    # Search button
    search_run_button = WebElement(css_selector='span[class="b-header-b-search-e-btntxt"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/books") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(xpath='//span[contains(text(), "Сначала дешевые"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//span[class="price-val"]/span')
