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


# def test_click_main_page_logo(web_browser):
#     page = MainPage(web_browser)
#     page.header_support.click()
#     page.main_page_logo.click()
#     assert page.current_url() == main_url


# def test_check_main_search(web_browser):
#     """ Make sure main search works fine. """
#
#     page = MainPage(web_browser)
#     page.search = user_search
#     page.search_run_button.click()
#
#     # Verify that user can see the list of products:
#     assert page.products_titles.count() > 0


# def test_check_wrong_input_in_search(web_browser):
#     """ Make sure that wrong keyboard layout input works fine. """
#
#     page = MainPage(web_browser)
#
#     # Try to enter "ОГЭ" with English keyboard:
#     page.search = 'огэ'
#     page.search_run_button.click()
#
#     # Verify that user can see the list of products:
#     assert page.products_titles.count() > 0
#
#     # Make sure user found the relevant products
#     for title in page.products_titles.get_text():
#         msg = 'Wrong product in search "{}"'.format(title)
#         assert 'огэ' in title.lower(), msg


# def test_open_games_window_from_footer(web_browser):
#     page = MainPage(web_browser)
#     page.scroll_down()
#     page.footer_games.click()
#     assert page.current_url() == main_url + 'games/'


# def test_open_reviews_window_from_footer(web_browser):
#     page = MainPage(web_browser)
#     page.scroll_down()
#     page.footer_reviews.click()
#     assert page.current_url() == main_url + 'reviews/'


# def test_open_best_page_from_footer(web_browser):
#     page = MainPage(web_browser)
#     page.scroll_down()
#     page.footer_best.click()
#     assert page.current_url() == main_url + 'best/'


# def test_open_partner_page_from_footer(web_browser):
#     page = MainPage(web_browser)
#     page.scroll_down()
#     page.footer_partner.click()
#     assert page.current_url() == partner_url


# def test_open_cabinet_page_from_footer(web_browser):
#     page = MainPage(web_browser)
#     page.scroll_down()
#     page.footer_cabinet.click()
#     assert page.current_url() == main_url + 'cabinet/'


# def test_open_support_page_from_footer(web_browser):
#     page = MainPage(web_browser)
#     page.scroll_down()
#     page.footer_support.click()
#     assert page.current_url() == main_url + 'support/'


def test_open_social_ok_from_footer(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.footer_social_ok.click()
    page.switch_to_window()
    assert page.current_url() == social_ok_url
