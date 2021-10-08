from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password") # селектор для пароля авторизации
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1") # пароль регистрации
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email") # селектор для регистрации почты
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2") #  повторный пароль регистрации
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit") # кнопка регистрации


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket") # селектор для добавления книги в корзину
    BOOK_NAME = (By.TAG_NAME, "h1") # селектор для названия книги
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong") # селектор для названия книги в сообщение
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color") # селектор для стоимости книги
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong") # селектор для стоимости книги в корзине
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner") # селектор для успешного сообщения

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # селектор для страницы авторизации
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") # селектор для подтверждение авторизации

class BasketPageLocators():
    LOOK_BASKET = (By.CSS_SELECTOR, '.btn-group a') # селектор для переход в корзину
    PRODUCT_ON_BASKET = (By.CLASS_NAME, "col-sm-6 h3" ) # селектор для  книги в корзине
    BASKET_EMPTY = (By.CSS_SELECTOR, ".content #content_inner p a") # селектор для того что корзина пуста

