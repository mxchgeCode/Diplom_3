from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
import allure


class OrderFeedPage(BasePage):
    @allure.step('Дождаться отображения заголовка Ленты заказов')
    def wait_and_check_displayed_title_of_orders_list(self):
        self.find_element_with_wait(OrderFeedPageLocators.TITLE_ORDER_FEED)
        return self.check_displaying_of_element(OrderFeedPageLocators.TITLE_ORDER_FEED)

    @allure.step('Кликнуть по первому заказу в ленте')
    def click_to_order_card(self):
        self.find_element_with_wait(OrderFeedPageLocators.FIRST_BURGER_CARD)
        self.click_to_element(OrderFeedPageLocators.FIRST_BURGER_CARD)

    @allure.step('Проверка отображение модального окна')
    def check_modal_window(self):
        self.find_element_with_wait(OrderFeedPageLocators.TITLE_MODAL_WINDOW)
        return self.check_displaying_of_element(OrderFeedPageLocators.TITLE_MODAL_WINDOW)

    @allure.step('Получить номер заказа в карточке')
    def get_id_order_card(self):
        return self.get_text_from_element(OrderFeedPageLocators.ID_ORDER_CARD)

    @allure.step('Проверить,что заказ существует в ленте заказов')
    def check_id_order_in_feed_order_list(self, order_id):
        locator = OrderFeedPageLocators.NUMBER_ORDER_IN_FEED_PAGE
        locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        self.find_element_with_wait(locator_with_order_id)
        return self.check_displaying_of_element(locator_with_order_id)

    @allure.step('Получить количество заказов за все время')
    def get_cnt_orders_all_time(self):
        self.find_element_with_wait(OrderFeedPageLocators.CNT_ORDERS_ALL_TIME)
        return self.get_text_from_element(OrderFeedPageLocators.CNT_ORDERS_ALL_TIME)

    @allure.step('Получить количество заказов за сегодня')
    def get_cnt_orders_today(self):
        self.find_element_with_wait(OrderFeedPageLocators.CNT_ORDERS_TODAY)
        return self.get_text_from_element(OrderFeedPageLocators.CNT_ORDERS_TODAY)

    @allure.step('Получить номер заказа в "В работе"')
    def get_number_from_order_in_work(self):
        return self.get_text_from_element(OrderFeedPageLocators.NUM_ORDER_IN_WORK)
