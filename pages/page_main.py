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

    @allure.step('Кликаем вопрос ')
    def click_question(self, question_id):
        locator = MainPageLocators.get_question_locator(question_id)
        self.click_via_script(locator)

    @allure.step('Получаем текст ответа на вопрос ')
    def get_answer_text(self, question_id):
        answer_locator = MainPageLocators.get_answer_locator(question_id)
        return self.get_element_text(answer_locator)
