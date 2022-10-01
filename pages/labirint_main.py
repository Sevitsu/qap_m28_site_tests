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

    # Main page Logo
    main_page_logo = WebElement(css_selector='span[class="b-header-b-logo-e-logo"]')

    # Auth window close
    auth_window_close = WebElement(css_selector='div[class="js-close-lab-modal new-auth__close header-sprite"]')

    # Page Header
    header_notify_btn = WebElement(css_selector='a[class="b-header-b-personal-e-link top-link-main have-dropdown-'
                                                'touchlink top-link-main_notification"]')
    header_putorder = WebElement(xpath='//a[@href = "/cabinet/putorder/"]')
    header_cart = WebElement(css_selector='a[class="b-header-b-personal-e-link top-link-main analytics-click-js'
                                          ' cart-icon-js"]')

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

    header_help = WebElement(css_selector='li[data-event-content="Доставка и оплата"]')
    header_certificates = WebElement(css_selector='li[data-event-content="Сертификаты"]')
    header_rating = WebElement(css_selector='li[data-event-content="Рейтинги"]')
    header_novelty = WebElement(css_selector='li[data-event-content="Новинки"]')
    header_sale = WebElement(css_selector='li[data-event-content="Скидки"]')
    header_contact = WebElement(css_selector='li[data-event-content="Контакты"]')


    # Personal login
    mylab_btn = WebElement(css_selector='span[class="b-header-b-personal-e-text '
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
