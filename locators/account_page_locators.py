from selenium.webdriver.common.by import By


class AccountPageLocators:
    LOGIN_BUTTON = (By.XPATH, '//button[ text()="Войти" ]')  # кнопка войти на странице login
    EMAIL_INPUT_FIELD_LOGIN = (By.XPATH, '//input[@name="name"]')
    PASSWORD_INPUT_FIELD_LOGIN = (By.XPATH, '//input[@name="Пароль"]')
    BUTTON_EXIT_FROM_ACCOUNT = (By.XPATH, '//button[contains(text(), "Выход")]')  # кнопка Выход из ЛК
    FEED_BUTTON = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    HISTORY_FEED_TODAY = (By.XPATH, '// p[contains(text(), "Выполнено за сегодня:")]')
    HISTORY_BUTTON = (By.CSS_SELECTOR, '//a[ text()="История заказов" ]')
