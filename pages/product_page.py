from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.add_button).click()

    def should_be_correct_product(self):
        assert self.browser.find_element(
            *ProductPageLocators.product_name
        ).text == self.browser.find_element(
            *ProductPageLocators.add_product_alert
        ).text, 'Название товара не совпадает'

    def should_be_correct_cost(self):
        assert self.browser.find_element(
            *ProductPageLocators.cost_alert
        ).text == self.browser.find_element(
            *ProductPageLocators.product_cost
        ).text, 'Цена товара не совпадает'
