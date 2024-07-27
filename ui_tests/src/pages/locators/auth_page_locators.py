from selenium.webdriver.common.by import By


class AuthPageLocators:
    """
    Класс, в котором содержатся локаторы для работы со страницей авторизации
    """

    URL = 'https://saas.saymon.info/#objects/66796a50c9bafa03840501f4/end-view'

    LOGIN_FIELD = (By.XPATH, '//input[@id="user-login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="user-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(@class, "js-native")]//span[normalize-space()="Войти"]')
