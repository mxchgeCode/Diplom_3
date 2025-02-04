import allure
from pages.home_page import HomePage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage


class TestHomePage:
    @allure.title('залогиненный пользователь может оформить заказ')
    def test_making_order_by_authenticated_user(self, driver, create_and_delete_user):
        email, password = create_and_delete_user
        account_page = AccountPage(driver)
        home_page = HomePage(driver)
        home_page.click_button_log_in_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()
        home_page.wait_visible_checkout_button()
        home_page.drag_and_drop_ingredient_to_basket()
        home_page.click_checkout_button()
        assert home_page.check_displaying_of_modal_window_after_create_order()

    @allure.title("Проверка переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        home_page = HomePage(driver)
        home_page.click_button_log_in_account()
        home_page.click_constructor_button()
        assert home_page.check_title_make_burger

    @allure.title("Проверка переход по клику на «Лента заказов»")
    def test_go_to_feed_orders(self, driver):
        home_page = HomePage(driver)
        feed_page = OrderFeedPage(driver)
        home_page.click_feed_button()
        assert feed_page.wait_and_check_displayed_title_of_orders_list()

    @allure.title("Проверка, если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_show_modal_window_details_after_click_of_ingredient(self, driver):
        home_page = HomePage(driver)
        home_page.click_ingredient_from_constructor()
        assert home_page.check_details_ingredient_modal_window()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_modal_window_details_of_ingredient(self, driver):
        home_page = HomePage(driver)
        home_page.click_ingredient_from_constructor()
        home_page.close_modal_window_details_ingredient()
        assert home_page.check_details_ingredient_modal_window_closed() is False

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_increase_counter_ingredient_if_add_ingedient(self, driver):
        home_page = HomePage(driver)
        home_page.drag_and_drop_ingredient_to_basket()
        assert home_page.get_counter_of_ingredients_in_basket() != 0
