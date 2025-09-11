from selenium.webdriver.common.by import By


class OrderLocators:

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']") # поле ввода Имя
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']") # поле ввода Фамилия
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # поле ввода Адрес

    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']") # поле ввода станции метро
    METRO_SAMPLE = (By.XPATH, "//li[contains(@class, 'select-search__row')]//div[contains(@class, 'Order_Text__2broi') and text()='Сокольники']/parent::button") # станция Сокольники в списке
    METRO_ALL_STATIONS = (By.CSS_SELECTOR, "li.select-search__row > button.Order_SelectOption__82bhS") # список всех станций

    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # поле ввода Телефон

    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Далее']") # кнопка Далее

    RENTAL_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # поле выбора даты
    RENTAL_DATE_CHOOSE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'react-datepicker__day--outside-month')) and text()='{}']") # плейсхолдер для выбора даты в календаре
    
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']") # поле Срок Аренды
    RENTAL_PERIOD_ALL_OPTIONS = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]") # список всех сроков аренды

    COLOR_BLACK = (By.XPATH, "//input[@id='black']") # чекбокс черный жемчуг
    COLOR_GREY = (By.XPATH, "//input[@id='grey']") # чекбокс серая безысходность

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # поле ввода Комментарий

    CONFIRMATION_HEADER = (By.CSS_SELECTOR, 'div[class^="Order_ModalHeader"]') # хэдер подтверждения заказа
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]") # кнопка подтверждения заказа ДА
    NOT_CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет')]") # кнопка НЕТ
    STATUS_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Посмотреть статус']") # кнопка Посмотреть статус в окне подтверждения заказа
