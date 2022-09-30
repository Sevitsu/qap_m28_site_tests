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
    header_books = WebElement(css_selector='li[data-toggle="header-genres"]')
    header_best = WebElement(css_selector='li[data-toggle="header-best"]')
    header_school = WebElement(css_selector='li[data-toggle="header-school"]')
    header_toys = WebElement(css_selector='li[data-toggle="header-toys"]')
    header_office = WebElement(css_selector='li[data-toggle="header-office"]')
    header_more = WebElement(css_selector='li[data-toggle="header-more"]')
    header_more_souvenir = WebElement(xpath='//a[@href = "/souvenir/" and '
                                            '@title = "Сувениры, альбомы для фотографий, фоторамки, календари."]')
    header_more_household = WebElement(xpath='//a[@href = "/household/" and @title = "Товары для дома"]')
    header_club = WebElement(xpath='//a[@href = "/club/" and @class = "b-header-b-menu-e-text"]')
    header_city_region = WebElement(css_selector='span[class = "b-header-b-menu-e-text js-header-menu-region-name"]')
    header_drp_region = WebElement(id='region-post')
    header_region_value = WebElement(id='region-post')

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
