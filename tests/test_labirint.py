#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*

import pytest
import time

from pages.labirint_main import MainPage
from config import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# def test_click_notifications_btn(web_browser):
#     page = MainPage(web_browser)
#     page.header_notify_btn.click()
#     page.auth_window_close.click()


# def test_login_window_open_close(web_browser):
#     page = MainPage(web_browser)
#     page.mylab_btn.click()
#     page.auth_window_close.click()


# def test_open_putorder_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_putorder.click()
#     assert page.current_url() == main_url + 'cabinet/putorder/'


# def test_open_cart_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_cart.click()
#     assert page.current_url() == main_url + 'cart/'


# def test_open_help_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_help.click()
#     assert page.current_url() == main_url + 'help/'


# def test_open_certificates_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_certificates.click()
#     assert page.current_url() == main_url + 'top/certificates/'


# def test_open_ratings_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_rating.click()
#     assert page.current_url() == main_url + 'rating/?id_genre=-1&nrd=1'


# def test_open_novelty_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_novelty.click()
#     assert page.current_url() == main_url + 'novelty/'


# def test_open_sale_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_sale.click()
#     assert page.current_url() == main_url + discount_url


# def test_open_contact_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_contact.click()
#     assert page.current_url() == main_url + 'contact/'


# def test_open_support_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_support.click()
#     assert page.current_url() == main_url + 'support/'


# def test_open_maps_window(web_browser):
#     page = MainPage(web_browser)
#     page.header_maps.click()
#     assert page.current_url() == main_url + 'maps/'


# def test_open_now_page(web_browser):
#     page = MainPage(web_browser)
#     page.header_recommend_btn.click()
#     assert page.current_url() == main_url + 'now/'


# def test_open_books_page(web_browser):
#     page = MainPage(web_browser)
#     page.header_books.click()
#     assert page.current_url() == main_url + 'books/'


# def test_open_best_page(web_browser):
#     page = MainPage(web_browser)
#     page.header_best.click()
#     assert page.current_url() == main_url + 'best/'


# def test_open_school_page(web_browser):
#     page = MainPage(web_browser)
#     page.header_school.click()
#     assert page.current_url() == main_url + 'school/'


# def test_open_toys_page(web_browser):
#     page = MainPage(web_browser)
#     page.header_toys.click()
#     assert page.current_url() == main_url + 'games/'


# def test_open_office_page(web_browser):
#     page = MainPage(web_browser)
#     page.header_office.click()
#     assert page.current_url() == main_url + 'office/'


# def test_open_souvenir_page(web_browser):
#     page = MainPage(web_browser)
#     page.header_more.click()
#     page.header_more_souvenir.click()
#     assert page.current_url() == main_url + 'souvenir/'


# def test_open_household_page(web_browser):
#     page = MainPage(web_browser)
#     page.header_more.click()
#     page.header_more_household.click()
#     assert page.current_url() == main_url + 'household/'


# def test_open_club_page(web_browser):
#     page = MainPage(web_browser)
#     page.header_club.click()
#     assert page.current_url() == main_url + 'club/'


# def test_change_region_name(web_browser):
#     page = MainPage(web_browser)
#     page.header_city_region.click()
#     page.header_drp_region.send_keys('Екатеринбург')
#     page.header_drp_region.send_keys(u'\ue007')
#     assert page.header_region_value.get_attribute('value') == "Екатеринбург"

# def test_click_main_page_logo(web_browser):
#     page = MainPage(web_browser)
#     page.main_page_logo.click()
#     assert page.current_url() == main_url


# def test_check_main_search(web_browser):
#     """ Make sure main search works fine. """
#
#     page = MainPage(web_browser)
#     time.sleep(9)
#
#     page.search = 'книга'
#     page.search_run_button.click()
#
#     # Verify that user can see the list of products:
#     assert page.products_titles.count() > 0
#
#     # Make sure user found the relevant products
#     for title in page.products_titles.get_text():
#         msg = 'Wrong product in search "{}"'.format(title)
#         assert 'книга' in title.lower(), msg


# def test_check_wrong_input_in_search(web_browser):
#     """ Make sure that wrong keyboard layout input works fine. """
#
#     page = MainPage(web_browser)
#     time.sleep(8)
#
#     # Try to enter "книга" with English keyboard:
#     page.search = 'rybuf'
#     time.sleep(3)
#     page.search_run_button.click()
#
#     # Verify that user can see the list of products:
#     assert page.products_titles.count() > 0
#
#     # Make sure user found the relevant products
#     for title in page.products_titles.get_text():
#         msg = 'Wrong product in search "{}"'.format(title)
#         assert 'книга' in title.lower(), msg
#
#
# @pytest.mark.xfail(reason="Filter by price doesn't work")
# def test_check_sort_by_price(web_browser):
#     """ Make sure that sort by price works fine.
#
#         Note: this test case will fail because there is a bug in
#               sorting products by price.
#     """
#
#     page = MainPage(web_browser)
#     time.sleep(8)
#
#     page.search = 'книга'
#     time.sleep(3)
#     page.search_run_button.click()
#
#     # Scroll to element before click on it to make sure
#     # user will see this element in real browser
#     page.sort_products_by_price.scroll_to_element()
#     page.sort_products_by_price.click()
#     page.wait_page_loaded()
#
#     # Get prices of the products in Search results
#     all_prices = page.products_prices.get_text()
#
#     # Convert all prices from strings to numbers
#     all_prices = [float(p.replace(' ', '')) for p in all_prices]
#
#     print(all_prices)
#     print(sorted(all_prices))
#
#     # Make sure products are sorted by price correctly:
#     assert all_prices == sorted(all_prices), "Sort by price doesn't work!"
