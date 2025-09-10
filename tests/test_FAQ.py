import allure
import pytest
from pages.base_page import *
from locators.faq_locators import *
from pages.faq_main_page import *

@allure.suite('Тесты вопросов и ответов')
class TestFAQ:

    @pytest.mark.parametrize("question,answer", [
    (FAQLocators.COST_QUESTION, FAQLocators.COST_ANSWER),
    (FAQLocators.MANY_SCOOTERS_QUESTION, FAQLocators.MANY_SCOOTERS_ANSWER),
    (FAQLocators.RENT_TIME_QUESTION, FAQLocators.RENT_TIME_ANSWER), 
    (FAQLocators.TODAY_QUESTION, FAQLocators.TODAY_ANSWER),
    (FAQLocators.CHANGE_TIME_QUESTION, FAQLocators.CHANGE_TIME_ANSWER),
    (FAQLocators.CHARGER_QUESTION, FAQLocators.CHARGER_ANSWER),
    (FAQLocators.CANCEL_QUESTION, FAQLocators.CANCEL_ANSWER),
    (FAQLocators.MKAD_QUESTION, FAQLocators.MKAD_ANSWER)
    ])

    @allure.title('Проверка раскрытия вопроса и появления ответа')
    def test_faq_question_show_answer(self, driver, question, answer):

        main_page = MainPageFAQ(driver)

        with allure.step('Кликнуть на вопрос'):
            main_page.click_on_question(question)

        with allure.step('Кликнуть на ответ'):
            main_page.click_on_answer(answer)
        
        with allure.step('Проверить раскрытие вопроса'):
            assert main_page.check_is_question_open(question), "Вопрос не раскрылся"

        with allure.step('Проверить соответствие ответа'):
            assert main_page.is_answer_visible(answer), "Ответ не соответствует ожидаемому"

   
