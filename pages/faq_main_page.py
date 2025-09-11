import allure
from selenium import webdriver
from pages.base_page import *
from locators.faq_locators import *

class MainPageFAQ(BasePage):

    @allure.step('Кликнуть на вопрос')
    def click_on_question(self, question):
        self.click_on_element(question)

    @allure.step('Проверить раскрытие вопроса')
    def check_is_question_open(self, question_locator):
        question = self.wait_for_element(question_locator)
        expanded_question = self.wait_for_element(FAQLocators.QUESTION_EXPANDED)
        return question == expanded_question
    
    @allure.step('Кликнуть на ответ')
    def click_on_answer(self, answer):
        self.click_on_element(answer)
    
    @allure.step('Проверить соответствие ответа')
    def is_answer_visible(self, answer_locator):
        return self.wait_for_element(answer_locator) is not None

