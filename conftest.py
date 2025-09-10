import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BaseLocators
from helpers.curl import *

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