from selenium.webdriver.common.by import By

class BaseLocators:

    ORDER_UPPER = (By.XPATH, "//button[starts-with(@class, 'Button_Button') and text()='Заказать' and not(contains(@class, 'Button_Middle'))]") # верхняя кнопка Заказать
    ORDER_LOWER = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']") # нижняя кнопка Заказать

    COOKIE_CONSENT = (By.ID, "rcc-confirm-button") # кнопка принятия куки

    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter') and @href='/']") # лого самоката
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex') and @href='//yandex.ru']") # лого яндекса

