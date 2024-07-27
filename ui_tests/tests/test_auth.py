from config.config import UserConfig
from ui_tests.src.enums.main_page_enums import OperationNames
from ui_tests.src.pages.auth_page import AuthPage
from ui_tests.src.pages.main_page import MainPage


class TestAuth:
    """
    Класс с тестами для страницы авторизации
    """

    def test_login_page(self, browser, logout):
        auth_page = AuthPage(browser=browser)
        main_page = MainPage(browser=browser)

        auth_page.open(auth_page.URL)

        auth_page.find_element_visibility(auth_page.LOGIN_FIELD).send_keys(UserConfig.USER_LOGIN.value)
        auth_page.find_element_visibility(auth_page.PASSWORD_FIELD).send_keys(UserConfig.USER_PASSWORD.value)
        auth_page.click_to_visible_element(auth_page.LOGIN_BUTTON)

        main_page.click_to_visible_element(
            main_page.get_button_apply_by_operation_name(operation_name=OperationNames.OPERATION_ONE.value)
        )
        main_page.check_add_operation_history()
