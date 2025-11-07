import pytest
from pages.page_order import OrderAuthorization
from data import UserData, UserDataTwo
import allure

class TestPageOder:

    @allure.story('Позитивный сценарий: заказ через верхнюю кнопку "Заказать"')
    @pytest.mark.parametrize("user_data,button_type", [
        (UserData, 'upper'),
        (UserDataTwo, 'upper')])
    def test_order_via_upper_button(self, driver, user_data, button_type):
        order = OrderAuthorization(driver)
        order.click_cookie_button()
        order.click_order_up_button(button_type)       
        order.input_name(user_data.NAME)
        order.input_surname(user_data.SURNAME)
        order.input_address(user_data.ADDRESS)
        order.select_metro(user_data.metro)
        order.input_phone(user_data.TELEPHONE)      
        order.click_next_button()      
        order.set_delivery_date(user_data.date)
        order.select_rent_period(user_data.rent)
        order.select_black_color()
        order.add_comment(user_data.comment)       
        order.confirm_order()
        order.accept_order()      
        # assert order.is_order_confirmed()
        order.verify_confirmation_text()
        assert order.is_order_confirmed()

    @allure.story('Позитивный сценарий: заказ через нижнюю кнопку "Заказать"')
    @pytest.mark.parametrize("user_data,button_type", [
        (UserData, 'lower'),
        (UserDataTwo, 'lower')])
    def test_order_via_lower_button(self, driver, user_data, button_type):
        order = OrderAuthorization(driver)
        order.click_cookie_button()
        order.scroll_to_button()
        order.click_order_low_button(button_type)
        order.input_name(user_data.NAME)
        order.input_surname(user_data.SURNAME)
        order.input_address(user_data.ADDRESS)
        order.select_metro(user_data.metro)
        order.input_phone(user_data.TELEPHONE)   
        order.click_next_button()
        order.set_delivery_date(user_data.date)
        order.select_rent_period(user_data.rent)
        order.select_black_color()
        order.add_comment(user_data.comment)
        order.confirm_order()
        order.accept_order()
        # assert order.is_order_confirmed()
        order.verify_confirmation_text()
        assert order.is_order_confirmed()