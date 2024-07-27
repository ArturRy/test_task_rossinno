from config.config import UserConfig
from ui_tests.src.pages.base_page import BasePage
from ui_tests.src.pages.locators.main_page_locators import MainPageLocators


class MainPage(BasePage, MainPageLocators):
    """
    Класс, в котором содержатся методы для работы с главной страницей
    """

    def check_add_operation_history(self):
        """
        Метод для проверки, что в блоке "История операций" отобразилась добавленная операция
        """

        assert (self.find_element_visibility
                (self.OPERATION_HISTORY_FIRST_ROW_OWNER
                 ).text == UserConfig.USER_LOGIN.value), 'В первой строке в ячейке "Пользователь" не отобразился логин'
        assert self.is_element_present(self.OPERATION_HISTORY_FIRST_ROW_RESULT_TEST), \
            'В первой строке в ячейке "Результаты" не отобразился текст "Test"'
