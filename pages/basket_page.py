from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_goods_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_CART_HEADER), \
            "Success message is presented, but should not be"

    def should_be_massage_about_empty_cart(self):
        empty_cart_massage = self.browser.find_element(*BasketPageLocators.EMPTY_CART_MESSAGE).text
        assert "Ваша корзина пуста" in empty_cart_massage, "There is no message about empty cart"
