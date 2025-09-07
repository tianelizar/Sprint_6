import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.helper import generate_order_data
from locators.base_page_locators import BaseLocators
from pages.order_page import OrderPage
from helpers.curl import *

@pytest.fixture(scope="class") 
def driver_class(request):
    options = Options()
    options.add_argument("--window-size=1200,600") 
    driver = webdriver.Firefox(options=options)
    driver.get(base_url)

    try:
        wait = WebDriverWait(driver, 10)
        consent_button = wait.until(EC.element_to_be_clickable(BaseLocators.COOKIE_CONSENT))
        consent_button.click()
    except Exception:
        pass

    request.cls.driver = driver
    request.cls.order_page = OrderPage(driver)  
    yield driver
    driver.quit()

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600") 
    driver = webdriver.Firefox(options=options)
    driver.get(base_url)

    try:
        wait = WebDriverWait(driver, 10)
        consent_button = wait.until(EC.element_to_be_clickable(BaseLocators.COOKIE_CONSENT))
        consent_button.click()
    except Exception:
        pass

    yield driver
    driver.quit()

@pytest.fixture
def order_data():
    return generate_order_data()