from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import LoginPageLocators

class ProductPage(BasePage):
    def should_be_added_thing_in_basket(self):
         self.add_product_to_basket()
         self.what_should_in_basket()
         self.should_be_same_price()
         self.messages_on_page()
         self.message_always_on_page()


    # добавление продукта в корзину
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    # возвращает название книги
    def return_name (self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        return book_name.text

    # возвращает цену книги
    def return_price (self):
        price_name = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return price_name.text

    # проверяем название книги в сообщенеи корзины
    def what_should_in_basket (self, book_name):
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME)
        assert alert_book_name.text == book_name, "Название книги{},а вот такое название книги в сообщение {}" .format(book_name,
                                                                                                                  alert_book_name.text)

    # проверяем цену книги в сообщенеи корзины
    def should_be_same_price(self, book_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text == book_price, "Цена в корзине {}, цена товара {}".format(basket_price.text,

                                                                                              book_price)
    # проверка отсутвия  успешного сообщения
    def messages_on_page(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented, but should not be"

    # проверка исчезновения успешного сообщения
    def message_always_on_page (self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщения нет"