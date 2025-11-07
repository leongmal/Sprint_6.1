from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_load_page(self):
        """ждем полной загрузки страницы"""
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def wait_for_visibility(self, locator):
        """Ждём видимости элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickability(self, locator):
        """Ждём кликабельного состояния элемента"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def input_text(self, locator, text):
        """Вводим данные в поле"""
        element = self.wait_for_visibility(locator)
        element.send_keys(text)

    def scroll_to_element(self, locator):
        """Скроллим до элемента"""
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
