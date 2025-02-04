from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    EMAIL_INPUT_FIELD = [By.XPATH, '//input[@name="name"]']
    PASSWORD_INPUT_FIELD = [By.XPATH, '//input[@name="Введите новый пароль"]']
    SAVE_BUTTON = [By.XPATH, '//input[@text="Сохранить"]']
    LOGIN_BUTTON = (By.XPATH, '//button[ text()="Войти" ]')  # кнопка войти на странице login
    # кнопка "Восстановить пароль" на странице login
    RECOVER_PASSWORD_LINK = (By.XPATH, '//a[ text()="Восстановить пароль" ]')
    # кнопка "Восстановить" на странице forgot-password
    RECOVER_BUTTON = (By.XPATH, '//button[ text()="Восстановить" ]')
    P_REMEMBER_PASS_QUESTION = (By.XPATH, '//p[ text()="Вспомнили пароль?" ]')
    # иконка отображения/скрытия пароля
    ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    ACTIVE_FIELD_AFTER_CLICK_ICON = (By.XPATH, '//div[contains(@class, "input_status_active")]')
