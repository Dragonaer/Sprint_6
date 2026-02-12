import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import url_dzen
from enum import StrEnum

class Answers(StrEnum):
    ANSWER_0 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    ANSWER_1 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    ANSWER_2 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ANSWER_3 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    ANSWER_4 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    ANSWER_5 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    ANSWER_6 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    ANSWER_7 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    

class MainPage(BasePage):
    @allure.step("Кликнуть на логотип Яндекса")
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageLocators.YA_LOGO_BUTTON)
        self.switch_to_window_by_index(-1)
        self.wait_for_page(url_dzen)

    @allure.step("Кликнуть на логотип Самокат")
    def click_on_logo_scooter(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER_MAINPAGE)
        self.click_on_element(MainPageLocators.SCOOTER_LOGO_BUTTON) 

    @allure.step("Кликнуть на вопрос из раздела Вопросы о важном")
    def click_on_question(self, heading):
        self.click_on_element(heading)





 