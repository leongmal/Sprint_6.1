from selenium.webdriver.common.by import By
# import pytest
# from data import Urls

class MainPageLocators:
    HOME_HEADER = (By.CLASS_NAME, "Home_Header__iJKdX")
    TITLE_IMPORTANT_QUESTIONS = (By.XPATH, "//div[text()='Вопросы о важном']")

    @staticmethod
    def get_question_locator(question_id):
        return (By.ID, f"accordion__heading-{question_id}")

    @staticmethod
    def get_answer_locator(question_id):
        return (By.XPATH, f"//*[@id='accordion__panel-{question_id}']/p")
