import allure
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_locators import OrderButtons


class OrderPage(BasePage):
    @allure.step("Нажать на кнопку Заказать")
    def click_on_order_form_button(self, button):
        self.scroll_to_element(button)
        self.click_on_element(button)

    @allure.step("Заполнить форму на первой странице заказа")
    def fill_first_page_order_form(self, name, lastname, adress, number):
        self.send_keys_to_input(OrderButtons.NAME, name)
        self.send_keys_to_input(OrderButtons.LAST_NAME, lastname)
        self.send_keys_to_input(OrderButtons.ADRESS, adress)
        self.click_on_element(OrderButtons.SUBWAY_STATION_BUTTON)
        self.click_on_element(OrderButtons.SUBWAY_STATION)
        self.send_keys_to_input(OrderButtons.NUMBER_PHONE, number)



    @allure.step("Нажать на кнопку далее на первой странице заказа")
    def click_on_father_button(self):
        self.click_on_element(OrderButtons.FARTHER_BUTTON)

    @allure.step("Заполнить форму на второй странице заказа, первый вариант")
    def fill_second_page_form_order_first_var(self, date):
        self.send_keys_to_input(OrderButtons.DATE, date)
        self.send_keys_to_input(OrderButtons.DATE, Keys.ENTER)
        self.click_on_element(OrderButtons.TERM)
        self.click_on_element(OrderButtons.TERM_ONE_DAY)
        self.click_on_element(OrderButtons.BLACK_COLOUR)

    @allure.step("Заполнить форму на второй странице заказа, второй вариант")
    def fill_second_page_form_order_second_var(self, date):
        self.send_keys_to_input(OrderButtons.DATE, date)
        self.click_on_element(OrderButtons.BODY)
        self.click_on_element(OrderButtons.TERM)
        self.click_on_element(OrderButtons.TERM_TWO_DAY)
        self.click_on_element(OrderButtons.GREY_COLOUR)

    @allure.step("Нажать на кнопку заказать на второй странице заказа")
    def click_on_order_button(self):
        self.click_on_element(OrderButtons.ORDER_BUTTON)

    @allure.step("Нажать на кнопку подтверждения заказа")
    def click_on_yes_button_in_validation(self):
        self.click_on_element(OrderButtons.YES_BUTTON)

    @allure.step("Получить текст всплывающего сообщения")
    def get_order_popup_text(self):
        return self.get_text_on_element(OrderButtons.STATUS_BUTTON)