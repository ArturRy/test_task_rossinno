from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Класс, в котором содержатся локаторы для работы с главной страницей
    """

    # Хедер

    LOGIN_NAME = (By.XPATH, '//div[@class="user-button-component"]//button')
    BUTTON_LOGOUT = (By.XPATH, '//a[@title="Выйти"]')

    #  Блок "История операций"

    OPERATION_HISTORY_FIRST_ROW_OWNER = (
        By.XPATH, '//div[@data-section="operations-history"]//tbody//tr[position()=1]//td[@class="owner"]'
    )
    OPERATION_HISTORY_FIRST_ROW_RESULT_TEST = (
        By.XPATH,
        '//div[@data-section="operations-history"]//tbody//tr[position()=1]//td[@class="description"]'
        '//span[contains(text(), "Test")]'
    )

    @staticmethod
    def get_button_apply_by_operation_name(operation_name):
        """
        Метод для получения локатора кнопки "Выполнить операцию" по названию операции
        :param operation_name: название операции
        :return: локатор (tuple)
        """

        return By.XPATH, (f'//div[@class="jarviswidget section-operations"]'
                          f'//td[normalize-space()="{operation_name}"]/parent::tr//button')
