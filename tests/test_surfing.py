import pytest
from pages.page_surfing import SurfIntern
from data import Urls
import allure


class TestSurfing:
    @allure.description("Проверить: если нажать на логотип Яндекса, в новом окне откроется главная страница Дзена")
    def test_yandex_logo_opens_dzen(self, driver):
        su = SurfIntern(driver)
        su.click_yandex_logo()
        su.wait_for_new_tab()
        su.switch_to_new_tab()
        final_url = su.get_dzen_url()

        assert Urls.DZEN in final_url


    @allure.description("Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»")
    def test_click_logo_scooter_to_page_home(self, main_page, driver):
        su = SurfIntern(driver)
        su.click_upper_order_button()
        su.click_scooter_logo()
        su.wait_for_home_page_load()
        final_url = su.get_current_url()

        assert Urls.SCOOTER == final_url
