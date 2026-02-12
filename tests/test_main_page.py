import allure

from pages.base_page import *
from pages.main_page import *
from pages.order_page import *
from helper import *
from curl import *

class TestMainPageLogoButton:
    @allure.title("Проверка перехода на сайт Яндекс.Дзен при клике на логотип Яндекса")
    def test_main_page_yandex_button(self, driver):
        self.driver = driver
        main_page = MainPage(driver)
        main_page.click_on_logo_yandex()
        assert main_page.url == url_dzen

    @allure.title("Проверка перехода на главную страницу сайта при клике на логотип Самоката")
    def test_main_page_scooter_button(self, driver):
        self.driver = driver
        main_page = MainPage(driver)
        main_page.click_on_logo_scooter()
        assert main_page.url == main_site

