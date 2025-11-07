# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from locators.locator_order import ElementFormRegisration, RegPage
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
# from data import UserData, UserDataTwo
import allure


class OrderAuthorization(BasePage):

    @allure.step('Клик по кнопке "Cookie"')
    def click_cookie_button(self):
        self.wait_for_clickability(ElementFormRegisration.COOCIE_BUTTON).click()

    @allure.step('Клик по верхней кнопке "Заказать" (тип: {button_type})')
    def click_order_up_button(self, button_type='upper'):
        locator = (ElementFormRegisration.UPPER_ORDER_BUTTON) 
        self.wait_for_clickability(locator).click()

    def scroll_to_button(self):
        self.scroll_to_element(ElementFormRegisration.LOWER_ORDER_BUTTON)

    @allure.step('Клик по нижней кнопке "Заказать" (тип: {button_type})')
    def click_order_low_button(self, button_type='lower'):
        locator = (ElementFormRegisration.LOWER_ORDER_BUTTON)
        self.wait_for_clickability(locator).click()    

    @allure.step('Ввод имени: {name}')
    def input_name(self, name):
        self.input_text(ElementFormRegisration.INPUT_FIELD_NAME, name)

    @allure.step('Ввод фамилии: {surname}')
    def input_surname(self, surname):
        self.input_text(ElementFormRegisration.INPUT_FIELD_SURNAME, surname)

    @allure.step('Ввод адреса: {address}')
    def input_address(self, address):
        self.input_text(ElementFormRegisration.INPUT_FIELD_ADDRESS, address)

    @allure.step('Выбор станции метро: {metro}')
    def select_metro(self, metro):
        input_locator = ElementFormRegisration.INPUT_FIELD_METRO
        self.wait_for_clickability(input_locator).click()
        metro_locator = RegPage.get_metro_selector(metro)
        self.wait_for_clickability(metro_locator).click()

    @allure.step('Ввод телефона: {phone}')
    def input_phone(self, phone):
        self.input_text(ElementFormRegisration.INPUT_FIELD_TELEPHONE, phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.wait_for_clickability(ElementFormRegisration.FURCHER_BUTTON).click()

    @allure.step('Указание даты доставки: {date}')
    def set_delivery_date(self, date):
        field = self.wait_for_clickability(ElementFormRegisration.INPUT_FIELD_WHEN)
        field.click()
        field.send_keys(date)
        field.send_keys(Keys.ENTER)

    @allure.step('Выбор периода аренды: {rent_period}')
    def select_rent_period(self, rent_period):
        self.wait_for_clickability(ElementFormRegisration.FILED_CHOICE_PERIOD_RENT).click()
        day_locator = RegPage.get_rent_day(rent_period)
        self.wait_for_clickability(day_locator).click()

    @allure.step('Выбор цвета самоката: чёрный')
    def select_black_color(self):
        self.wait_for_clickability(ElementFormRegisration.CHECK_BOX_BLACK).click()

    @allure.step('Добавление комментария для курьера: {comment}')
    def add_comment(self, comment):
        self.input_text(ElementFormRegisration.FIELD_COMMENT, comment)

    @allure.step('Финальное оформление заказа')
    def confirm_order(self):
        self.wait_for_clickability(ElementFormRegisration.ORDER_BUTTON).click()

    @allure.step('Подтверждение заказа кнопкой "Да"')
    def accept_order(self):
        self.wait_for_clickability(ElementFormRegisration.YES_BUTTON).click()

    @allure.step('Проверка видимости сообщения "Заказ оформлен"')
    def is_order_confirmed(self):
        return self.wait_for_visibility(ElementFormRegisration.VISUAL_STATUS).is_displayed()

    @allure.step('Получение текста подтверждения заказа')
    def get_confirmation_text(self):
        return self.wait_for_visibility(ElementFormRegisration.VISUAL_STATUS).text

    @allure.step('Сверка текста подтверждения с ожидаемым: {expected_text}')
    def verify_confirmation_text(self, expected_text="Посмотреть статус"):
        actual_text = self.get_confirmation_text()
        assert actual_text == expected_text




