import pytest
from pages.page_surfing import SurfIntern
from data import Urls
from locators.locator_order import ElementFormRegisration
import allure



class TestSurfing:
    @allure.description("Проверить: при клике на логотип Яндекса открывается страница Дзена в новой вкладке")
    def test_yandex_logo_opens_dzen(self, driver):
        # driver.get(Urls.SCOOTER)
        su = SurfIntern(driver)
        su.wait_for_home_page_load()
        su.click_yandex_logo()
        su.wait_for_new_tab()
        su.switch_to_new_tab()
        su.wait_for_load_page()
        final_url = su.get_dzen_url()
        assert Urls.DZEN in final_url


    @allure.description("Проверить: клик по логотипу Самоката ведёт на главную страницу Самоката")
    def test_click_logo_scooter_to_page_home(self, driver):

        su = SurfIntern(driver)
        su.wait_for_home_page_load()
        su.wait_for_clickability(ElementFormRegisration.UPPER_ORDER_BUTTON).click()
        su.click_scooter_logo()
        su.wait_for_home_page_load()
        final_url = su.get_current_url()
        assert Urls.SCOOTER == final_url
