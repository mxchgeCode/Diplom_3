import pytest
from pages.password_recovery_page import PasswordRecoveryPage
from pages.home_page import HomePage
import allure


class TestPasswordRecoveryPage:
    @allure.title("Проверка переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_go_to_password_recovery_page(self, browser):
        password_recovery_page = PasswordRecoveryPage(browser)
        home_page = HomePage(browser)
        home_page.click_button_log_in_account()
        password_recovery_page.click_button_recover_password()
        assert password_recovery_page.check_displaying_of_p_question

    @allure.title("Проверка перехода на url reset_password,после ввод почты и клика по кнопке «Восстановить")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_go_to_reset_password_page(self, browser):
        password_recovery_page = PasswordRecoveryPage(browser)
        home_page = HomePage(browser)
        home_page.click_button_log_in_account()
        password_recovery_page.click_button_recover_password()
        password_recovery_page.send_data_email()
        password_recovery_page.click_button_recover()
        assert password_recovery_page.check_displaying_of_save_button

    @allure.title("Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    @allure.description("При клике по иконке показать/скрыть значение атрибута инпута становится 'password'")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_active_border_after_click_icon(self, browser):
        password_recovery_page = PasswordRecoveryPage(browser)
        home_page = HomePage(browser)
        home_page.click_button_log_in_account()
        password_recovery_page.click_button_recover_password()
        password_recovery_page.send_data_email()
        password_recovery_page.click_button_recover()
        password_recovery_page.wait_visibility_of_icon()
        password_recovery_page.click_icon()
        assert password_recovery_page.check_displaying_active_border()
