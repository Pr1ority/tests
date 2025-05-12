from selenium.webdriver.common.by import By


class LoginPageLocatots:
    login_form = (By.ID, 'login_form')
    register_form = (By.ID, 'register_form')


class ProductPageLocators:
    add_button = (By.CLASS_NAME, 'btn-add-to-basket')
    product_name = (By.TAG_NAME, 'h1')
    add_product_alert = (By.CSS_SELECTOR, '#messages strong')
    product_cost = (By.CSS_SELECTOR, '.product_main > .price_color')
    cost_alert = (By.CSS_SELECTOR, '.alertinner > p > strong')
    success_message = (By.CLASS_NAME, 'alertinner')


class BasePageLocators:
    login_link = (By.CSS_SELECTOR, "#login_link")
    login_link_invalid = (By.CSS_SELECTOR, "#login_link_inc")
    basket_link = (By.CSS_SELECTOR, '.basket-mini .btn-default')


class BasketPageLocators:
    product_image = (By.TAG_NAME, 'img')
    basket_empty = (By.CSS_SELECTOR, '#content_inner > p')
