import time

import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.authorized_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = ProductPage(
            browser,
            'http://selenium1py.pythonanywhere.com/ru'
            '/catalogue/the-shellcoders-handbook_209/'
        )
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + '@fakemail.org'
        login_page.register_new_user(email=email, password='testpassword')
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(
            browser,
            'http://selenium1py.pythonanywhere.com/ru'
            '/catalogue/the-shellcoders-handbook_209/'
        )
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(
            browser,
            'http://selenium1py.pythonanywhere.com/ru'
            '/catalogue/the-shellcoders-handbook_209/'
        )
        page.open()
        page.add_product_to_cart()
        page.should_be_correct_cost()
        page.should_be_correct_product()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/ru'
        '/catalogue/the-shellcoders-handbook_209/'
    )
    page.open()
    page.add_product_to_cart()
    page.should_be_correct_cost()
    page.should_be_correct_product()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser
        ):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/ru'
        '/catalogue/the-shellcoders-handbook_209/'
    )
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/ru'
        '/catalogue/the-shellcoders-handbook_209/'
    )
    page.open()
    page.add_product_to_cart()
    page.success_message_should_dissapear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/en-gb/'
        'catalogue/the-city-and-the-stars_95/'
    )
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/en-gb/'
        'catalogue/the-city-and-the-stars_95/'
    )
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/en-gb/'
        'catalogue/the-city-and-the-stars_95/'
    )
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.should_be_basket_empty_text()
