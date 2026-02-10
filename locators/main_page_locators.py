from selenium.webdriver.common.by import By

class MainPageLocators:
    """основные локаторы на главной странице"""
    ORDER_BUTTON_HEADER_MAINPAGE = (By.CLASS_NAME, 'Button_Button__ra12g') #кнопка "Заказать" вверху страницы
    ORDER_BUTTON_MIDDLE_MAINPAGE = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")#кнопка "Заказать" в центре страницы
    SCOOTER_LOGO_BUTTON = (By.XPATH, '//img[@alt="Scooter"]') #логотип "Самокат"
    YA_LOGO_BUTTON = (By.XPATH, '//img[@alt="Yandex"]') #логотип "Яндекс"
    COOKIE_BUTTON = (By.XPATH, "//button[contains(text(),'да все привыкли')]") #кнопка куки



