from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


