import pytest
from playwright.sync_api import Page, expect

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    password_input = chromium_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill("password")

    login_button = chromium_page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.locator(
        '//div[@data-testid="login-page-wrong-email-or-password-alert"]'
    )
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    chromium_page.wait_for_timeout(5000)
