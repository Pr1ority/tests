from selenium.webdriver.common.by import By


class LoginPageLocators:
    login_form = (By.ID, 'login_form')
    register_form = (By.ID, 'register_form')
    register_email = (By.CSS_SELECTOR, '[name=registration-email]')
    register_password = (By.CSS_SELECTOR, '[name=registration-password1]')
    register_password_repeat = (
        By.CSS_SELECTOR,
        '[name=registration-password2]'
    )
    register_button = (By.NAME, 'registration_submit')


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
    user_icon = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    product_image = (By.TAG_NAME, 'img')
    basket_empty = (By.CSS_SELECTOR, '#content_inner > p')
