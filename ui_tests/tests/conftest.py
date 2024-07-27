import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.src.pages.main_page import MainPage


@pytest.fixture()
def browser():
    """
    Подключение драйвера в начале теста и закрытие его в конце
    """

    options = Options()
    prefs = dict()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    browser.quit()


@pytest.fixture()
def logout(browser):
    yield
    main_page = MainPage(browser=browser)
    main_page.click_to_visible_element(main_page.LOGIN_NAME)
    main_page.click_to_visible_element(main_page.BUTTON_LOGOUT)
