from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')
        self.user_already_exists_alert = page.get_by_test_id('registration-page-user-already-exists-alert')

    def fill_registration_form(self, email: str, password: str, username: str):
        self.registration_form.email_input.fill(email)
        expect(self.registration_form.email_input).to_have_value(email)

        self.registration_form.username_input.fill(username)
        expect(self.registration_form.username_input).to_have_value(username)

        self.registration_form.password_input.fill(password)
        expect(self.registration_form.password_input).to_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()

    def check_visible_user_already_exists_alert(self):
        expect(self.user_already_exists_alert).to_be_visible()
        expect(self.user_already_exists_alert).to_have_text("User already exists")