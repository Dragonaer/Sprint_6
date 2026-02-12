import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.base_page import *
from pages.main_page import *
from pages.order_page import *
from helper import *


class TestOrderButtons:
    @allure.title('Проверка перехода на форму заказа через кнопки в начале страницы и середины странице')
    @allure.description("Используются валидные данные")
    @pytest.mark.parametrize('button, fill_second_page', [
        (MainPageLocators.ORDER_BUTTON_HEADER_MAINPAGE, OrderPage.fill_second_page_form_order_first_var),
        (MainPageLocators.ORDER_BUTTON_MIDDLE_MAINPAGE, OrderPage.fill_second_page_form_order_second_var),
        ])
    
    def test_first_order_button_on_header_mainpage(self, driver, button, fill_second_page):
        order_page = OrderPage(driver)
        name, lastname, adress, number = generate_registration_data()
        date = generate_random_date()
        order_page.click_on_cookie_button()
        order_page.click_on_order_form_button(button)
        order_page.fill_first_page_order_form(name, lastname, adress, number)
        order_page.click_on_father_button()
        fill_second_page(order_page, date)
        order_page.click_on_order_button()
        order_page.click_on_yes_button_in_validation()
        text_order_popup = order_page.get_order_popup_text()

        assert text_order_popup == 'Посмотреть статус'


