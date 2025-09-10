import allure
import pytest
from pages.order_page import OrderPage
from locators.base_page_locators import *
from locators.order_page_locators import *
from helpers.helper import *
from helpers.curl import *

@allure.suite('Тесты в форме заказа')
class TestOrderFlow:

    @allure.title("Проверка полного флоу заказа")
    @pytest.mark.parametrize("order_button, order_data", [(BaseLocators.ORDER_UPPER, order_data_1), (BaseLocators.ORDER_LOWER, order_data_2)])
    def test_order_buttons_show_order_page(self, driver, order_button, order_data):

        order_page = OrderPage(driver)

        with allure.step('Кликнуть по кнопке Заказать'):
            order_page.click_on_element(order_button)
            order_page.wait_for_order_page() 

        with allure.step('Заполнить поле Имя'):
            order_page.click_on_name()
            order_page.fill_name(order_data["name"])
            
        with allure.step('Заполнить поле Фамилия'):
            order_page.click_on_surname()
            order_page.fill_surname(order_data["surname"])

        with allure.step('Заполнить поле Адрес'):
            order_page.click_on_address()
            order_page.fill_address(order_data["address"])

        with allure.step('Выбрать случайную станцию из списка метро'):
            order_page.open_metro_list()
            order_page.choose_random_station()

        with allure.step('Заполнить поле Телефон'):
            order_page.click_on_phone()
            order_page.fill_phone(order_data["phone"])

        with allure.step('Кликнуть на кнопку Далее'):
            order_page.click_next()

        with allure.step('Выбрать случайную дату аренды в календаре'):
            order_page.open_calendar()
            order_page.choose_random_day(order_data["random_day"])

        with allure.step('Выбрать случайный срок аренды'):
            order_page.open_period_list()
            order_page.choose_random_period()

        with allure.step('Выбрать случайные цвета самоката'):
            order_page.choose_random_colors()

        with allure.step('Заполнить поле Комментарий'):
            order_page.click_on_comment()
            order_page.fill_comment(order_data["comment"])

        with allure.step('Кликнуть по нижней кнопке Заказать'):
            order_page.click_order_lower()

        with allure.step('Подтвердить заказ'):
            order_page.confirm_order()

        with allure.step('Проверить сообщение об успешном заказе'):
            assert order_page.is_successful_popup(), "Сообщение об успешном заказе не появилось"

@allure.suite('Тесты в форме заказа')
class TestLogos:

    @allure.title('Переход на главную страницу по клику на логотип самоката')
    def test_scooter_logo_show_main_page(self, driver):
        
        order_page = OrderPage(driver)

        with allure.step('Кликнуть по верхней кнопке Заказать'):
            order_page.click_order_upper()

        with allure.step('Кликнуть на логотип самоката'):
            order_page.click_on_scooter()
        
        with allure.step('Проверить адрес главной страницы'):
            assert order_page.is_main_page(), "Не на главной странице"

    @allure.title('Редирект на Дзен по клику на логотип Яндекса')
    def test_yandex_logo_redirect_to_dzen(self, driver):

        order_page = OrderPage(driver)

        with allure.step('Кликнуть на логотип Яндекса'):
            order_page.click_on_yandex()

        with allure.step('Проверить редирект на Дзен'):
            assert order_page.is_dzen()

