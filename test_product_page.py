import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):

        email = str(time.time()) + "@fakemail.org"   # создание имейла для регистрации
        password = str(time.time())   # создание пароля для регистрации
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"     # переход на авторизацию
        self.login_page = LoginPage(browser, link)   # передаем в конструктор экземпляр драйвера и url адрес
        self.login_page.open()    # открываем страницу
        self.login_page.go_to_login_page()    # открываем страницу авторизации
        self.login_page.register_new_user(email, password)   # вводим пароль и имейл
        self.login_page.should_be_authorized_user()    # проверяем что авторизованы

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_product_to_basket()  # жмем кнопку добавление в корзину
        page.solve_quiz_and_get_code()  # происходит магия (получаем код)
        page.what_should_in_basket(page.return_name()) # проверяем что лежит в корзине
        page.should_be_same_price(page.return_price()) # проверяем цену того  что лежит в корзине
        time.sleep(10)

    @pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.messages_on_page()  # проверка отсутвия  успешного сообщения

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket( browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()    # открываем страницу
    page.add_product_to_basket()
    page.messages_on_page()  # проверка отсутвия  успешного сообщения

@pytest.mark.need_review
def test_guest_can_add_product_to_basket( browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product_to_basket()  # жмем кнопку добавление в корзину
    page.what_should_in_basket(page.return_name())    # проверяем что лежит в корзине
    page.should_be_same_price(page.return_price())    # проверяем цену того  что лежит в корзине
    time.sleep(10)

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()   # открываем страницу
    page.add_product_to_basket()   # добавление продукта в корзину
    page.message_always_on_page()   # сообщение в корзине


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()    # открываем страницу
    page.should_be_login_link()   # проверка наличия ссылки авторизации на страницу

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()    # открываем страницу
    page.go_to_login_page()  # открываем страницу авторизации

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()    # открываем страницу
    page.basket_open()   # переходим в корзину
    page.basket_without_product()  # проверяем что в корзине нет товаров
    page.message_always_on_page()  # проверяем  наличие сообщения о пустоте корзины