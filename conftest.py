import pytest
from selenium import webdriver
from pages.page_main import MainPage
# from locators.locator_main import MainPageLocators
from data import Urls

@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    browser.get(Urls.SCOOTER)
    yield browser
    browser.quit()



@pytest.fixture(scope="function")
def main_page(driver):
    page = MainPage(driver)
    page.wait_for_load_page()
    # page.wait_for_load_page(MainPageLocators.TITLE_IMPORTANT_QUESTIONS)
    return page
