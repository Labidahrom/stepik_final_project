from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "div#messages>div:nth-child(1) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, "div#messages>div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_ICON = (By.CSS_SELECTOR, "span a.btn.btn-default")

class BasketPageLocators():
    ITEMS_IN_CART_HEADER = (By.CSS_SELECTOR, "h2.col-sm-6.h3")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")




