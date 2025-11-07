
from pages.base_page import BasePage
from locators.locator_dz_scoot import Surfing_the_Internet
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator_order import ElementFormRegisration
import time
import allure


class SurfIntern(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.original_window = None  # Инициализируем заранее

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        self.original_window = self.driver.current_window_handle
        self.wait_for_clickability(Surfing_the_Internet.BUTTON_YANDEX).click()

    @allure.step("Ждём появления новой вкладки")
    def wait_for_new_tab(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_new_tab(self):
        new_window = [w for w in self.driver.window_handles if w != self.original_window][0]
        self.driver.switch_to.window(new_window)

    @allure.step("Проверяем, что URL содержит 'dzen.ru'")
    def get_dzen_url(self, timeout=15):
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_url = self.driver.current_url
            if "dzen.ru" in current_url:
                return current_url
            time.sleep(0.5)


    @allure.step("Кликаем по кнопке «Заказать» (верхняя)")
    def click_upper_order_button(self):
        order_button = self.wait_for_clickability(ElementFormRegisration.UPPER_ORDER_BUTTON)
        order_button.click()

    @allure.step("Кликаем по логотипу «Самоката»")
    def click_scooter_logo(self):
        logo = self.wait_for_clickability(Surfing_the_Internet.BUTTON_SCOOTER)
        logo.click()

    @allure.step("Ждём полной загрузки главной страницы")
    def wait_for_home_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url
