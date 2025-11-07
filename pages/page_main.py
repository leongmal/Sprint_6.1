from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locator_main import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    @allure.step('Ждём полной загрузки страницы')
    def wait_for_page_load(self):
        self.wait_for_load_page()

    @allure.step('Прокручивает страницу до элемента')
    def scroll_to_element(self, locator):
        self.wait_for_visibility(MainPageLocators.TITLE_IMPORTANT_QUESTIONS)

    @allure.step('Ждём кликабельного состояния и кликаем элемент')
    def click_question(self, question_id):
        locator = MainPageLocators.get_question_locator(question_id)
        element= self.wait_for_clickability(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ждём видимости ответа')
    def get_answer_text(self, question_id):
        answer_locator = MainPageLocators.get_answer_locator(question_id)
        return self.wait_for_visibility(answer_locator).text
