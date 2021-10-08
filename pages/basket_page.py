from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):


    #проверка наличия товара в корзине
    def basket_without_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ON_BASKET),\
        "в корзине есть товар"

    # проверка что корзина пуста
    def message_always_on_page (self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "Корзина не пуста"