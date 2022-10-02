from config import *
from pages.labirint_auth_page import AuthPage
import pyautogui


def test_login_window_input(web_browser):
    page = AuthPage(web_browser)
    page.mylab_btn.click()
    page.input_field_1.send_keys(random_email)
    page.submit_btn.click()
    page.auth_window_close.click()
    assert page.current_url() == main_url


def test_auth_code_input(web_browser):
    page = AuthPage(web_browser)
    page.mylab_btn.click()
    page.input_field_1.send_keys(random_email)
    page.submit_btn.click()
    page.Auth_code_field.click()
    page.Auth_code_field.send_keys(auth_code)
    pyautogui.press("tab")
    pyautogui.press("enter")
    page.incorrect_auth_code_note.find()
    page.incorrect_auth_code_note.is_visible()
