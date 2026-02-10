import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_locators import OrderButtons


class OrderPage(BasePage):

    @allure.step("Нажать на кнопку Заказать вверху страницы")
    def click_on_order_in_header_page(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER_MAINPAGE)

    @allure.step("Нажать на кнопку Заказать в середине страницы")
    def click_on_order_on_the_middle_page(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE_MAINPAGE)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_MIDDLE_MAINPAGE)

    @allure.step("Заполнить форму на первой странице заказа, первый вариант")
    def fill_first_page_form_order_first_var(self, name, lastname, adress, number):
        self.send_keys_to_input(OrderButtons.NAME, name)
        self.send_keys_to_input(OrderButtons.LAST_NAME, lastname)
        self.send_keys_to_input(OrderButtons.ADRESS, adress)
        self.click_on_element(OrderButtons.SUBWAY_STATION_BUTTON)
        self.click_on_element(OrderButtons.SUBWAY_STATION_1)
        self.send_keys_to_input(OrderButtons.NUMBER_PHONE, number)

    @allure.step("Заполнить форму на первой странице заказа, второй вариант")
    def fill_first_page_form_order_second_var(self, name, lastname, adress, number):
        self.send_keys_to_input(OrderButtons.NAME, name)
        self.send_keys_to_input(OrderButtons.LAST_NAME, lastname)
        self.send_keys_to_input(OrderButtons.ADRESS, adress)
        self.click_on_element(OrderButtons.SUBWAY_STATION_BUTTON)
        self.click_on_element(OrderButtons.SUBWAY_STATION_2)
        self.send_keys_to_input(OrderButtons.NUMBER_PHONE, number)


    @allure.step("Нажать на кнопку далее на первой странице заказа")
    def click_on_father_button(self):
        self.click_on_element(OrderButtons.FARTHER_BUTTON)

    @allure.step("Заполнить форму на второй странице заказа, первый вариант")
    def fill_second_page_form_order_first_var(self, date):
        self.send_keys_to_input(OrderButtons.DATE, date)
        self.click_on_element(OrderButtons.BODY)
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