import allure

from pages.base_page import *
from pages.main_page import *
from pages.order_page import *
from helper import *


class TestOrderButtons:
    @allure.title('Проверка перехода на форму заказа через кнопку в начале страницы')
    @allure.description("Используются валидные данные с проверкой кликабельности Черного цвета самоката")
    def test_first_order_button_on_header_mainpage(self, driver):
        order_page = OrderPage(driver)
        name, lastname, adress, number = generate_registration_data()
        date = generate_random_date()
        order_page.click_on_cookie_button()
        order_page.click_on_order_in_header_page()
        order_page.fill_first_page_form_order_first_var(name, lastname, adress, number)
        order_page.click_on_father_button()
        order_page.fill_second_page_form_order_first_var(date)
        order_page.click_on_order_button()
        order_page.click_on_yes_button_in_validation()
        text_order_popup = order_page.get_order_popup_text()

        assert text_order_popup == 'Посмотреть статус'

    @allure.title('Проверка перехода на форму заказа через кнопку в середине страницы')
    @allure.description("Используются валидные данные с проверкой кликабельности Серого цвета самоката")
    def test_second_order_button_on_middle_mainpage(self, driver):
        order_page = OrderPage(driver)
        name, lastname, adress, number = generate_registration_data()
        date = generate_random_date()
        order_page.click_on_cookie_button()
        order_page.click_on_order_on_the_middle_page()
        order_page.fill_first_page_form_order_second_var(name, lastname, adress, number)
        order_page.click_on_father_button()
        order_page.fill_second_page_form_order_second_var(date)
        order_page.click_on_order_button()
        order_page.click_on_yes_button_in_validation()
        text_order_popup = order_page.get_order_popup_text()

        assert text_order_popup == 'Посмотреть статус'
