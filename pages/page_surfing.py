from pages.base_page import BasePage
from locators.locator_dz_scoot import Surfing_the_Internet
from locators.locator_order import ElementFormRegisration
import allure



class SurfIntern(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.original_window = None

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        self.original_window = self.current_window_handle()
        self.wait_for_clickability(Surfing_the_Internet.BUTTON_YANDEX).click()

    @allure.step("Ждём появления новой вкладки")
    def wait_for_new_tab(self):
        super().wait_for_new_tab(min_windows=2)

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_new_tab(self):
        all_windows = self.get_window_handles()
        new_window = [w for w in all_windows if w != self.original_window]
        self.switch_to_window(new_window[0])

    @allure.step("Проверяем, что URL содержит 'dzen.ru'")
    def get_dzen_url(self):
        self.wait_for_url_contains("dzen.ru")
        return self.get_current_url()

    @allure.step("Кликаем по кнопке «Заказать» (верхняя)")
    def click_upper_order_button(self):
        self.wait_for_clickability(ElementFormRegisration.UPPER_ORDER_BUTTON).click()

    @allure.step("Кликаем по логотипу «Самоката»")
    def click_scooter_logo(self):
        self.wait_for_clickability(Surfing_the_Internet.BUTTON_SCOOTER).click()

    @allure.step("Ждём загрузки главной страницы")
    def wait_for_home_page_load(self):
        self.wait_for_load_page(timeout=10)
