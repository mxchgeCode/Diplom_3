from pages.account_page import AccountPage
from pages.home_page import HomePage
import allure


class TestAccountPage:
    @allure.title("Проверка переход по клику на «Личный кабинет»")
    def test_go_to_account_page(self, driver, create_and_delete_user):
        email, password = create_and_delete_user
        account_page = AccountPage(driver)
        home_page = HomePage(driver)
        home_page.click_button_log_in_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()
        home_page.wait_visible_checkout_button()
        home_page.click_personal_account_link()
        assert account_page.check_exit_button()

    @allure.title("Проверка выход из аккаунта")
    def test_exit_from_account_page(self, driver, create_and_delete_user):
        email, password = create_and_delete_user
        account_page = AccountPage(driver)
        home_page = HomePage(driver)
        home_page.click_button_log_in_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()
        home_page.wait_visible_checkout_button()
        home_page.click_personal_account_link()
        account_page.check_exit_button()
        account_page.click_exit_button()
        account_page.wait_visible_login_button()
        assert account_page.check_displaying_of_login_button()

    @allure.title("Проверка переход в раздел «История заказов»")
    def test_go_to_history_orders(self, driver, create_and_delete_user):
        email, password = create_and_delete_user
        account_page = AccountPage(driver)
        home_page = HomePage(driver)
        home_page.click_button_log_in_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()
        home_page.wait_visible_checkout_button()
        home_page.click_personal_account_link()
        account_page.click_feed_button()
        account_page.wait_visible_history_feed()
        assert account_page.check_history_feed()
