from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time



class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_load_page(self, timeout=10):
        """Ждём полной загрузки страницы"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def wait_for_visibility(self, locator):
        """Ждём видимости элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickability(self, locator):
        """Ждём кликабельного состояния элемента"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def input_text(self, locator, text):
        """Вводим текст в поле"""
        element = self.wait_for_visibility(locator)
        element.send_keys(text)

    def scroll_to_element(self, locator):
        """Прокручиваем до элемента"""
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",element)

    def click_via_script(self, locator):
        """Кликаем через JS"""
        element = self.wait_for_clickability(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_element_text(self, locator):
        """Получаем текст элемента"""
        element = self.wait_for_visibility(locator)
        return element.text

    def find_element(self, locator):
        """Находим элемент"""
        return self.driver.find_element(*locator)

    def get_current_url(self):
        """Получаем текущий URL"""
        return self.driver.current_url

    def get_window_handles(self):
        """Список дескрипторов окон"""
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        """Переключаемся на окно"""
        self.driver.switch_to.window(window_handle)

    def current_window_handle(self):
        """Дескриптор текущего окна"""
        return self.driver.current_window_handle


    def wait_for_new_tab(self, min_windows=2, timeout=15):
        """Ждём появления минимум min_windows вкладок"""
        # WebDriverWait(self.driver, timeout).until(
        #     lambda d: len(d.window_handles) >= min_windows)
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: len(d.window_handles) >= min_windows)

    def wait_for_url_contains(self, substring, timeout=15):
        """Ждём, пока URL содержит подстроку"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            if substring in self.get_current_url():
                return
            time.sleep(0.5)
        raise TimeoutError(f"URL не содержит '{substring}' за {timeout} сек.")
