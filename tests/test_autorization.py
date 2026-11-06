import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_page = LoginPage(chromium_page)

    login_page.login_form.fill(email, password)
    login_page.login_button_click()
    login_page.check_visible_wrong_email_or_password_alert()
