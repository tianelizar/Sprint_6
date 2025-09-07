from selenium.webdriver.common.by import By

class FAQLocators:
    
    COST_QUESTION = (By.XPATH, "//div[@id='accordion__heading-0' and contains(text(),'Сколько это стоит?')]") # сколько это стоит - вопрос
    COST_ANSWER = (By.XPATH, "//p[contains(text(),'Сутки — 400 рублей')]") # сколько это стоит - ответ

    MANY_SCOOTERS_QUESTION = (By.XPATH, "//div[@id='accordion__heading-1' and contains(text(),'Хочу сразу несколько')]") # несколько самокатов - вопрос
    MANY_SCOOTERS_ANSWER = (By.XPATH, "//p[contains(text(),'один заказ — один самокат')]") # несколько самокатов - ответ
    
    RENT_TIME_QUESTION = (By.XPATH, "//div[@id='accordion__heading-2' and contains(text(),'Как рассчитывается время')]") # время аренды - вопрос
    RENT_TIME_ANSWER = (By.XPATH, "//p[contains(text(),'Отсчёт времени аренды')]") # время аренды - ответ
    
    TODAY_QUESTION = (By.XPATH, "//div[@id='accordion__heading-3' and contains(text(),'прямо на сегодня')]") # заказать сегодня - вопрос
    TODAY_ANSWER = (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего')]") # заказать сегодня - ответ
    
    CHANGE_TIME_QUESTION = (By.XPATH, "//div[@id='accordion__heading-4' and contains(text(),'Можно ли продлить заказ')]") # продлить или вернуть - вопрос
    CHANGE_TIME_ANSWER = (By.XPATH, "//p[contains(text(),'Пока что нет!')]") # продлить или вернуть - ответ
    
    CHARGER_QUESTION = (By.XPATH, "//div[@id='accordion__heading-5' and contains(text(),'Вы привозите зарядку')]") # зарядка - вопрос
    CHARGER_ANSWER = (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой')]") # зарядка - ответ
    
    CANCEL_QUESTION = (By.XPATH, "//div[@id='accordion__heading-6' and contains(text(),'Можно ли отменить заказ?')]") # отменить заказ - вопрос
    CANCEL_ANSWER = (By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли')]") # отменить заказ - ответ
    
    MKAD_QUESTION = (By.XPATH, "//div[@id='accordion__heading-7' and contains(text(),'за МКАДом')]") # заказ за МКАД - вопрос
    MKAD_ANSWER = (By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов!')]") # заказ за МКАД - ответ

    QUESTION_EXPANDED = (By.XPATH, "//div[starts-with(@id, 'accordion__heading') and @aria-expanded='true']") # вопрос раскрылся

