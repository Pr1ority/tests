from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, (
            'Неккоректная ссылка, должна быть ссылка на логин'
        )

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.login_form
        ), 'Отсутствует форма логина'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.register_form
        ), 'Отсутствует форма регистрации'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.register_email).send_keys(
            email
        )
        self.browser.find_element(
            *LoginPageLocators.register_password
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.register_password_repeat
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.register_button
        ).click()
