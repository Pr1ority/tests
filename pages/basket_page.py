from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.product_image
        ), 'В корзине есть товары, хотя их быть не должно'

    def should_be_basket_empty_text(self):
        assert self.is_element_present(
            *BasketPageLocators.basket_empty
        ), 'Нет текста о том, что корзина пуста'
