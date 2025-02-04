from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
import allure
from utils.helper import *


class PasswordRecoveryPage(BasePage):
    @allure.step('Кликнуть по кнопке "Восстановить пароль" на странице login')
    def click_button_recover_password(self):
        self.click_to_element(PasswordRecoveryPageLocators.RECOVER_PASSWORD_LINK)

    @allure.step('Проверка есть ли p с вопросом "Вспомнили пароль?"')
    def check_displaying_of_p_question(self):
        return self.find_element_with_wait(PasswordRecoveryPageLocators.P_REMEMBER_PASS_QUESTION)

    @allure.step('Проверка отображения кнопки "Сохранить"')
    def check_displaying_of_save_button(self):
        return self.find_element_with_wait(PasswordRecoveryPageLocators.SAVE_BUTTON)

    @allure.step('Ввести Email')
    def send_data_email(self):
        email = create_random_creds()['email']
        self.send_keys_to_input(PasswordRecoveryPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Кликнуть по кнопке "Восстановить"')
    def click_button_recover(self):
        self.click_to_element(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    @allure.step('Подождать прогрузки иконки показать/скрыть пароль')
    def wait_visibility_of_icon(self):
        self.find_element_with_wait(PasswordRecoveryPageLocators.ICON)

    @allure.step('Кликнуть по иконке показать/скрыть пароль')
    def click_icon(self):
        self.click_to_element(PasswordRecoveryPageLocators.ICON)

    @allure.step('Получить значение атрибута type="password" иконки показать/скрыть')
    def get_type_attr_icon(self):
        return self.find_element_with_wait(PasswordRecoveryPageLocators.ICON).get_attribute('type')

    @allure.step('Проверка появления рамка после клика по иконке глаза')
    def check_displaying_active_border(self):
        return self.find_element_with_wait(PasswordRecoveryPageLocators.ACTIVE_FIELD_AFTER_CLICK_ICON)
