import pytest
import allure

from locators.questions_locators import QuestionSection
from pages.base_page import *
from pages.main_page import *



class TestImportQuestions:
    @allure.title("Тест кликабельности Вопросов о важном")
    @pytest.mark.parametrize('accordion_id', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_questions_button(self, driver, accordion_id):
        main_page = MainPage(driver)
        main_page.click_on_cookie_button()
        section = QuestionSection(accordion_id)
        main_page.click_on_question(section.heading)
        assert main_page.check_attr(section.panel, 'hidden') is None

