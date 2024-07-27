from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.src.enums.global_enums import TimeoutEnum


class BasePage:
    """
    Базовый класс, от которого наследуются классы всех страниц в проекте. Этот класс содержит базовую логику для
    всех страниц проекта
    """

    def __init__(self, browser):
        self.browser = browser

    def find_element_visibility(self, locator, timeout_for_wait=TimeoutEnum.TEN_SEC.value):
        """
        Метод для поиска элементов с настройкой ожидания, пока элемент не станет видимым
        """

        try:
            element = WebDriverWait(self.browser, timeout_for_wait).until(
                EC.visibility_of_element_located(locator)
            )
            return element

        except TimeoutException as ex:
            raise ex

    def find_elements_visibility(self, locator, timeout_for_wait=TimeoutEnum.ONE_AND_A_HALF_SEC.value):
        """
        Метод для поиска списка элементов с настройкой ожидания, пока все элементы станут видимыми
        """

        try:
            elements = WebDriverWait(self.browser, timeout_for_wait).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return elements

        except TimeoutException:
            return []

    def find_element_clickable(self, locator, timeout_for_wait=TimeoutEnum.TEN_SEC.value):
        """
        Метод для поиска элементов с настройкой ожидания, пока элемент не станет кликабельным
        """

        try:
            element = WebDriverWait(self.browser, timeout_for_wait).until(
                EC.element_to_be_clickable(locator)
            )
            return element

        except TimeoutException as ex:
            raise ex

    def click_to_visible_element(self, locator, timeout_for_wait=TimeoutEnum.TEN_SEC.value):
        """
        Метод для клика по элементу, когда он станет видимым
        """

        self.find_element_visibility(locator, timeout_for_wait).click()

    def click_to_clickable_element(self, locator, timeout_for_wait=TimeoutEnum.TEN_SEC.value):
        """
        Метод для клика по элементу, когда он станет кликабельным
        """

        self.find_element_clickable(locator, timeout_for_wait).click()

    def is_element_present(self, locator, timeout_for_wait=TimeoutEnum.TEN_SEC.value):
        """
        Метод, проверяющий наличие элемента на странице
        """

        try:
            self.find_element_visibility(locator, timeout_for_wait)
        except TimeoutException:
            return False
        return True

    def is_element_not_present(self, locator, timeout_for_wait=TimeoutEnum.ONE_SEC.value):
        """
        Метод, проверяющий отсутствие элемента на странице
        """

        try:
            self.find_element_visibility(locator, timeout_for_wait)
        except TimeoutException:
            return True
        return False

    def open(self, url):
        """
        Метод для открытия браузером указанного url
        """

        self.browser.get(url)

    def complete(self):
        """
        Метод, возвращающий True, когда страница загрузилась
        """

        return self.browser.execute_script("return document.readyState == 'complete';")

    def is_disappeared(self, locator, timeout_for_wait=TimeoutEnum.SIXTY_SEC.value):
        """
        Метод для проверки, что элемент исчез со страницы
        """

        try:
            WebDriverWait(self.browser, timeout_for_wait).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True
