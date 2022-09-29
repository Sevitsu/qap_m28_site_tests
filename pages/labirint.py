#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os
from config import main_url
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or main_url

        super().__init__(web_driver, url)

    # Page Header
    main_page_logo = WebElement(css_selector='span[class="b-header-b-logo-e-logo"]')
    header_recommend_btn = WebElement(css_selector='span[class="itm-md-vis-hdn itm-lg-vis-shw"]')
    current_url = WebPage.get_current_url

    # Personal login
    login_btn = WebElement(css_selector='span[class="b-header-b-personal-e-text '
                                        'b-header-b-personal-e-text-m-overflow"]')
    input_field_1 = WebElement(id='_inputnamecode_2')

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
