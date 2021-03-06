from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import time
import pytest
import random

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_right_book('Coders at Work')
    page.should_be_right_price('19,99 £')

@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart()
#     page.solve_quiz_and_get_code()
#     page.should_disappeared()
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_cart_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_not_be_goods_in_the_cart()
#     basket_page.should_be_massage_about_empty_cart()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        generate_email = str(random.randint(1, 100)) + str(random.randint(1, 1000)) + "aa@yandex.ru"
        page.register_new_user(generate_email, "Khfu23438z")
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_be_right_book("Coders at Work")
        page.should_be_right_price('19,99 £')

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_not_be_success_message()




