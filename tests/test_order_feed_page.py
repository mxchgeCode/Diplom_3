import pytest
from pages.home_page import HomePage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage
import allure
import time


class TestOrderFeedPage:
    @allure.step('Проверка, если кликнуть на заказ, откроется всплывающее окно')
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_opening_modal_window(self, browser):
        feed_page = OrderFeedPage(browser)
        home_page = HomePage(browser)
        home_page.click_feed_button()
        feed_page.click_to_order_card()
        assert feed_page.check_modal_window()

    @allure.title('Проверка,что заказы пользователя из раздела "История заказов"'
                  ' отображаются на странице «Лента заказов»')
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_displaying_in_feed_new_order_from_history(self, browser, create_and_delete_user):
        email, password = create_and_delete_user
        account_page = AccountPage(browser)
        feed_page = OrderFeedPage(browser)
        home_page = HomePage(browser)

        home_page.click_button_log_in_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()

        home_page.wait_visible_checkout_button()
        home_page.drag_and_drop_ingredient_to_basket(browser)
        time.sleep(5)
        home_page.click_checkout_button()
        time.sleep(5)
        home_page.close_order_window()

        home_page.go_feed_page()
        time.sleep(2)
        order_id = feed_page.get_id_order_card()
        assert feed_page.check_id_order_in_feed_order_list(order_id)

    @allure.title('Проверка при создании нового заказа счётчик Выполнено за "всё время" увеличивается')
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_inc_counter_all_time_of_orders(self, browser, create_and_delete_user):
        email, password = create_and_delete_user
        account_page = AccountPage(browser)
        feed_page = OrderFeedPage(browser)
        home_page = HomePage(browser)

        home_page.click_feed_button()
        orders_cnt_1 = feed_page.get_cnt_orders_all_time()

        home_page.click_constructor_button()
        home_page.click_button_log_in_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()

        home_page.wait_visible_checkout_button()
        home_page.drag_and_drop_ingredient_to_basket(browser)
        time.sleep(5)
        home_page.click_checkout_button()
        time.sleep(10)
        home_page.close_order_window()

        home_page.go_feed_page()
        time.sleep(2)
        orders_cnt_2 = feed_page.get_cnt_orders_all_time()
        assert orders_cnt_2 > orders_cnt_1

    @allure.title('Проверка при создании нового заказа счётчик Выполнено за "сегодня" увеличивается')
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_inc_counter_of_today_orders(self, browser, create_and_delete_user):
        email, password = create_and_delete_user
        account_page = AccountPage(browser)
        feed_page = OrderFeedPage(browser)
        home_page = HomePage(browser)

        home_page.go_feed_page()
        time.sleep(5)
        orders_cnt_1 = feed_page.get_cnt_orders_today()
        home_page.click_constructor_button()

        home_page.click_button_log_in_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()

        home_page.drag_and_drop_ingredient_to_basket(browser)

        home_page.wait_visible_checkout_button()
        home_page.click_checkout_button()
        time.sleep(10)
        home_page.close_order_window()

        home_page.go_feed_page()
        time.sleep(2)
        orders_cnt_2 = feed_page.get_cnt_orders_today()
        assert orders_cnt_2 > orders_cnt_1, f"Счетчик заказов не увеличился: {orders_cnt_1} -> {orders_cnt_2}"

    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_check_displaying_new_order_in_work(self, browser, create_and_delete_user):
        email, password = create_and_delete_user
        account_page = AccountPage(browser)
        feed_page = OrderFeedPage(browser)
        home_page = HomePage(browser)
        home_page.click_button_log_in_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()
        home_page.drag_and_drop_ingredient_to_basket(browser)
        time.sleep(2)
        home_page.wait_visible_checkout_button()
        home_page.click_checkout_button()
        time.sleep(10)
        new_order_id = home_page.get_number_in_modal_window_after_create_order()
        home_page.close_order_window()
        home_page.go_feed_page()
        time.sleep(2)
        assert feed_page.get_number_from_order_in_work() == f'0{new_order_id}'
