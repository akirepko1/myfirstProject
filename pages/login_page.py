
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url
        assert True

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Авторизоваться не возможно нет формы авторизации"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Зарегистрироваться  не возможно нет формы авторизации"
        assert True

    def register_new_user(self, email, password):
        email_adress = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        email_adress.send_keys(email)
        password_on = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_on.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        password_confirm.send_keys(password)
        click_on_register = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        click_on_register.click()

