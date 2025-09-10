import allure
import random
from selenium import webdriver
from pages.base_page import *
from helpers.helper import *
from locators.base_page_locators import *
from locators.order_page_locators import *
from helpers.curl import *

class OrderPage(BasePage):

    @allure.step('Подождать загрузки страницы заказа')
    def wait_for_order_page(self):
        return self.wait_for_element(OrderLocators.NAME_INPUT)
    
    @allure.step('Проверить адрес страницы заказа')
    def is_order_page(self):
        return self.is_expected_page(order_url)

    @allure.step('Кликнуть по верхней кнопке Заказать')
    def click_order_upper(self):
        self.click_on_element(BaseLocators.ORDER_UPPER)

    @allure.step('Кликнуть по нижней кнопке Заказать')
    def click_order_lower(self):
        self.scroll_to_element(BaseLocators.ORDER_LOWER)
        self.click_on_element(BaseLocators.ORDER_LOWER)

    @allure.step('Кликнуть на поле Имя')
    def click_on_name(self):
        self.click_on_element(OrderLocators.NAME_INPUT)

    @allure.step('Заполнить поле Имя')
    def fill_name(self, name):
        self.send_keys_to_input(OrderLocators.NAME_INPUT, name)

    @allure.step('Кликнуть на поле Фамилия')
    def click_on_surname(self):
        self.click_on_element(OrderLocators.SURNAME_INPUT)

    @allure.step('Заполнить поле Фамилия')
    def fill_surname(self, surname):
        self.send_keys_to_input(OrderLocators.SURNAME_INPUT, surname)

    @allure.step('Кликнуть на поле Адрес')
    def click_on_address(self):
        self.click_on_element(OrderLocators.ADDRESS_INPUT)

    @allure.step('Заполнить поле Адрес')
    def fill_address(self, address):
        self.send_keys_to_input(OrderLocators.ADDRESS_INPUT, address)

    @allure.step('Открыть список станций метро')
    def open_metro_list(self):
        self.click_on_element(OrderLocators.METRO_INPUT)

    @allure.step('Выбрать станцию вводом с клавиатуры')
    def choose_sample_station(self):
        self.send_keys_to_input(OrderLocators.METRO_INPUT, 'Сокольники')
        self.click_on_element(OrderLocators.METRO_SAMPLE)

    @allure.step('Выбрать случайную станцию')
    def choose_random_station(self):
        stations = self.wait_for_elements(OrderLocators.METRO_ALL_STATIONS)        
        if not stations:
            raise Exception("Станции метро не найдены в списке")
        random_station = random.choice(stations)
        self.scroll_to_element(random_station)
        self.click_on_element(random_station)

    @allure.step('Кликнуть на поле Телефон')
    def click_on_phone(self):
        self.click_on_element(OrderLocators.PHONE_INPUT)

    @allure.step('Заполнить поле Телефон')
    def fill_phone(self, phone):
        self.send_keys_to_input(OrderLocators.PHONE_INPUT, phone)

    @allure.step('Кликнуть на кнопку Далее')
    def click_next(self):
        self.click_on_element(OrderLocators.NEXT_BUTTON)

    @allure.step('Проверить переход на вторую часть формы')
    def is_second_part(self):
        return self.wait_for_element(OrderLocators.RENTAL_DATE)

    @allure.step('Открыть календарь')
    def open_calendar(self):
        self.click_on_element(OrderLocators.RENTAL_DATE)

    @allure.step('Выбрать случайную дату')
    def choose_random_day(self, random_day):
        day_locator = (OrderLocators.RENTAL_DATE_CHOOSE[0], OrderLocators.RENTAL_DATE_CHOOSE[1].format(random_day))
        self.click_on_element(day_locator)

    @allure.step('Раскрыть список сроков аренды')
    def open_period_list(self):
        self.click_on_element(OrderLocators.RENTAL_PERIOD)

    @allure.step('Выбрать случайный срок аренды')
    def choose_random_period(self):
        period_options = self.wait_for_elements(OrderLocators.RENTAL_PERIOD_ALL_OPTIONS)
        random_period = random.choice(period_options)
        self.click_on_element(random_period)

    @allure.step('Выбрать случайные цвета самоката')
    def choose_random_colors(self):
        colors = [OrderLocators.COLOR_BLACK, OrderLocators.COLOR_GREY]
        for locator in random.sample(colors, k=random.randint(0, 2)):
            self.click_on_element(locator)

    @allure.step('Кликнуть на поле Комментарий')
    def click_on_comment(self):
        self.click_on_element(OrderLocators.COMMENT_INPUT)

    @allure.step('Заполнить поле Комментарий')
    def fill_comment(self, comment):
        self.send_keys_to_input(OrderLocators.COMMENT_INPUT, comment)

    @allure.step('Проверить появление всплывающего окна подтверждения заказа')
    def is_confirmation_popup(self):
        return self.wait_for_element(OrderLocators.CONFIRM_BUTTON)
    
    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_on_element(OrderLocators.CONFIRM_BUTTON)

    @allure.step('Отменить заказ')
    def cancel_order(self):
        self.click_on_element(OrderLocators.NOT_CONFIRM_BUTTON)

    @allure.step('Проверить сообщение об успешном заказе')
    def is_successful_popup(self):
        return self.wait_for_element(OrderLocators.STATUS_BUTTON)
    
    @allure.step('Кликнуть на логотип самоката')
    def click_on_scooter(self):
        self.click_on_element(BaseLocators.LOGO_SCOOTER)

    @allure.step('Проверить адрес главной страницы')
    def is_main_page(self):
        return self.is_expected_page(base_url)

    @allure.step('Кликнуть на логотип Яндекса')
    def click_on_yandex(self):
        self.click_on_element(BaseLocators.LOGO_YANDEX)

    @allure.step('Проверить редирект на Дзен')
    def is_dzen(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains(dzen_url))
        return dzen_url in self.driver.current_url