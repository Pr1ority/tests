from selenium.webdriver.common.by import By


class MainPageLocators:
    login_link = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocatots:
    login_form = (By.ID, 'login_form')
    register_form = (By.ID, 'register_form')
