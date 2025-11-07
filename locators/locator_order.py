from selenium.webdriver.common.by import By


class ElementFormRegisration:
    """Локаторы элементов для формы оформления заказа"""

    """ Элементы главной страницы """
    # UPPER_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')  # Верхняя кнопка «Заказать»
    UPPER_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")  # Верхняя кнопка «Заказать»
    COOCIE_BUTTON = (By.CLASS_NAME, 'App_CookieButton__3cvqF')  # Кнопка «Да, все привыкли» (куки)
    LOWER_ORDER_BUTTON = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM')  # Нижняя кнопка «Заказать»


    """ Элементы страницы «Для кого самокат» """
    INPUT_FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле «Имя»
    INPUT_FIELD_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле «Фамилия»
    INPUT_FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле «Адрес»
    INPUT_FIELD_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Поле «Станция метро»
    METRO_SELECTOR = "//div[text()='{metro}']/parent::button"  # Шаблон XPath для выбора станции метро
    INPUT_FIELD_TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле «Телефон»
    FURCHER_BUTTON = (By.XPATH,"//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Далее']")  # Кнопка «Далее»


    """ Элементы страницы «Про аренду» """
    INPUT_FIELD_WHEN = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле «Когда привезти самокат»
    FILED_CHOICE_PERIOD_RENT = (By.CLASS_NAME, 'Dropdown-arrow')  # Выпадающий список срока аренды
    CHOICE_PERIOD_RENT = "//div[text()='{rent}']"  # Шаблон XPath для выбора срока аренды
    CHECK_BOX_BLACK = (By.ID, 'black')  # Чекбокс «Чёрный»
    CHECK_BOX_GREEN = (By.ID, 'grey')  # Чекбокс «Серая безысходность»
    FIELD_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Поле «Комментарий для курьера»
    ORDER_BUTTON = (By.XPATH,"//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")  # Кнопка «Заказать» на странице аренды


    """ Элементы формы подтверждения заказа """
    YES_BUTTON = (By.XPATH,"//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']")  # Кнопка «Да» в диалоговом окне
    TITLE_ORDER_OK = (By.XPATH,"//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")  # Заголовок «Заказ оформлен»
    VISUAL_STATUS = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text() = 'Посмотреть статус']") # Кнопка с надписью "Посмтреть статус"





class RegPage:
    """Вспомогательные методы для формирования динамических локаторов"""

    @staticmethod
    def get_metro_selector(metro_value: str) -> tuple:
        """ Возвращает XPath-локатор для выбранной станции метро. """
        formatted_xpath = ElementFormRegisration.METRO_SELECTOR.format(metro=metro_value)
        return (By.XPATH, formatted_xpath)


    @staticmethod
    def get_rent_day(rent_value: str) -> tuple:
        """ Возвращает XPath-локатор для выбранного срока аренды. """
        formatted_xpath = ElementFormRegisration.CHOICE_PERIOD_RENT.format(rent=rent_value)
        return (By.XPATH, formatted_xpath)
