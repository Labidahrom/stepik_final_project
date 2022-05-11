from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_cart_button.click()

    def get_item_name_in_cart(self):
        item_in_cart = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        return item_in_cart

    def should_be_right_book(self, book_name):
        assert book_name in self.get_item_name_in_cart(), "Incorrect book"

    def get_item_price_in_cart(self):
        item_prict_in_cart = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        return item_prict_in_cart

    def should_be_right_price(self, book_price):
        assert self.get_item_price_in_cart() == book_price, "Incorrect price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        

