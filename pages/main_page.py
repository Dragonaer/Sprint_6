import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import url_dzen


class MainPage(BasePage):
    @allure.title("Кликнуть на логотип Яндекса")
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageLocators.YA_LOGO_BUTTON)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_for_page(url_dzen)

    @allure.title("Кликнуть на логотип Самокат")
    def click_on_logo_scooter(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER_MAINPAGE)
        self.click_on_element(MainPageLocators.SCOOTER_LOGO_BUTTON) 

    @allure.title("Кликнуть на вопрос из раздела Вопросы о важном")
    def click_on_question(self, heading):
        self.click_on_element(heading)





 