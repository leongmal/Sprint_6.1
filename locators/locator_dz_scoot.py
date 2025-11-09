from selenium.webdriver.common.by import By

class Surfing_the_Internet:

    BUTTON_SCOOTER = (By.CSS_SELECTOR, 'a[href="/"] img[alt="Scooter"]')
    BUTTON_TO_FIND  = (By.CLASS_NAME, 'arrow__button')
    BUTTON_YANDEX = (By.CSS_SELECTOR, 'a[href*="yandex.ru"]')
