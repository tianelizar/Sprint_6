import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Подождать видимости элемента
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

   # Скролл до элемента
    def scroll_to_element(self, element_or_locator):
        if isinstance(element_or_locator, tuple):
            element = self.wait_for_element(element_or_locator)
        else:
            element = element_or_locator  
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('Кликнуть на элемент')
    def click_on_element(self, element_or_locator, timeout=10):
        if isinstance(element_or_locator, tuple):  # ожидаем локатор
            element = self.wait_for_element(element_or_locator, timeout)
        else:
            element = element_or_locator  
        element.click()


   # Подождать видимости элементов
    def wait_for_elements(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    
   # Ввести текст в поле ввода
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    # Проверить, что адрес страницы совпадает с ожидаемым
    def is_expected_page(self, expected_url):
        return expected_url in self.driver.current_url
    
    @allure.step('Перейти в окно редиректа')
    def switch_to_tab(self, target_url):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains(target_url))
        
    
    