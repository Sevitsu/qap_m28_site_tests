from pages.base import WebPage
from pages.elements import WebElement
from config import main_url


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = main_url
        super().__init__(web_driver, url)

    current_url = WebPage.get_current_url

    # Personal login
    mylab_btn = WebElement(css_selector='span[class="b-header-b-personal-e-text '
                                        'b-header-b-personal-e-text-m-overflow"]')

    input_field_1 = WebElement(css_selector='input[placeholder="Введите свой код скидки, телефон или эл.почту"]')
    password = WebElement(id='pass')
    submit_btn = WebElement(id='g-recap-0-btn')
    Auth_code_field = WebElement(css_selector='input[placeholder="Введите свой код скидки"]')
    check_code_btn = WebElement(css_selector='input[type="submit"]')
    incorrect_auth_code_note = WebElement(css_selector='small[class="full-input__msg-small js-msg-small"]')

    # Auth window close
    auth_window_close = WebElement(css_selector='div[class="js-close-lab-modal new-auth__close header-sprite"]')
