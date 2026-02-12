import pytest
import allure

from locators.questions_locators import QuestionSection
from pages.base_page import *
from pages.main_page import *


class TestImportQuestions:
    @allure.title("Тест кликабельности Вопросов о важном")
    @pytest.mark.parametrize('accordion_id, answer', [
        (0, Answers.ANSWER_0), 
        (1, Answers.ANSWER_1), 
        (2, Answers.ANSWER_2), 
        (3, Answers.ANSWER_3), 
        (4, Answers.ANSWER_4), 
        (5, Answers.ANSWER_5), 
        (6, Answers.ANSWER_6), 
        (7, Answers.ANSWER_7),
    ])

    def test_questions_button(self, driver, accordion_id, answer):
        main_page = MainPage(driver)
        main_page.click_on_cookie_button()
        section = QuestionSection(accordion_id)
        main_page.click_on_question(section.heading)
        assert main_page.check_attr(section.panel, 'hidden') is None
        assert answer == main_page.get_text_on_element(section.panel)

