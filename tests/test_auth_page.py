import pytest
from pages.auth_page import AuthPage


def test_authorisation_success(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys('qwer@mmm.ru')
    page.password.send_keys("567")

    page.btn.click()

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'
