from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from data import URLs
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure


class HomePage(BasePage):
    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_button_log_in_account(self):
        self.click_to_element(HomePageLocators.SIGN_IN_ACCOUNT_BUTTON)

    @allure.step('Кликнуть по кнопке "Оформить заказ" на главной')
    def click_checkout_button(self):
        self.click_to_element(HomePageLocators.CHECKOUT_BUTTON)

    @allure.step('Кликнуть по кнопке "Личный кабинет" на главной')
    def click_personal_account_link(self):
        self.click_to_element(HomePageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Проверка видимости кнопки Оформить заказ')
    def wait_visible_checkout_button(self):
        self.find_element_with_wait(HomePageLocators.CHECKOUT_BUTTON)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_feed_button(self):
        self.find_element_with_wait(HomePageLocators.FEED_BUTTON)
        self.click_to_element(HomePageLocators.FEED_BUTTON)

    @allure.step('Переход к разделу "Лента заказов"')
    def go_feed_page(self):
        self.driver.get(f'{URLs.BASE_URL}{URLs.FEED_PAGE_URL}')

    @allure.step('Кликнуть по кнопке конструктора')
    def click_constructor_button(self):
        self.click_to_element(HomePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверка отображение заголовка "Соберите бургер"')
    def check_title_make_burger(self):
        return self.click_to_element(HomePageLocators.MAKE_BURGER_TITLE)

    @allure.step('Кликнуть по ингредиенту в конструкторе')
    def click_ingredient_from_constructor(self):
        self.find_element_with_wait(HomePageLocators.INGREDIENT_FROM_CONSTRUCTOR)
        self.click_to_element(HomePageLocators.INGREDIENT_FROM_CONSTRUCTOR)

    @allure.step('Проверка,что модальное окно "Детали ингредиента" появилось')
    def check_details_ingredient_modal_window(self):
        self.find_element_with_wait(HomePageLocators.DETAILS_OF_INGREDIENT)
        return self.check_displaying_of_element(HomePageLocators.DETAILS_OF_INGREDIENT)

    @allure.step('Клик по крестику для закрытия модального окна "Детали ингредиента"')
    def close_modal_window_details_ingredient(self):
        self.find_element_with_wait(HomePageLocators.BUTTON_CLOSE_MODAL_WINDOW_DETAILS_ING)
        self.click_to_element(HomePageLocators.BUTTON_CLOSE_MODAL_WINDOW_DETAILS_ING)

    @allure.step('Проверка,что модальное окно "Детали ингредиента" закрыто')
    def check_details_ingredient_modal_window_closed(self):
        self.find_element_with_wait(HomePageLocators.DETAILS_OF_INGREDIENT)
        return not self.check_displaying_of_element(HomePageLocators.DETAILS_OF_INGREDIENT)

    @allure.step('Перетащить ингредиент в конструктор бургера в корзине')
    def drag_and_drop_ingredient_to_basket(self, browser):
        source = self.find_element_with_wait(HomePageLocators.INGREDIENT_FROM_CONSTRUCTOR)
        target = self.find_element_with_wait(HomePageLocators.BURGER_CONSTRUCTOR_BASKET)
        browser.execute_script(
            "function createEvent(type) { var event = document.createEvent('CustomEvent'); "
            "event.initCustomEvent(type, true, true, null); return event; } function dispatchEvent(element,"
            " event, transferData) { if (element.dispatchEvent) { element.dispatchEvent(event); } else "
            "if (element.fireEvent) { element.fireEvent('on' + event.type, event); } } var source = arguments[0];"
            " var target = arguments[1]; var dragStartEvent = createEvent('dragstart'); dispatchEvent(source,"
            " dragStartEvent); var dropEvent = createEvent('drop'); dispatchEvent(target, dropEvent); var "
            "dragEndEvent = createEvent('dragend'); dispatchEvent(source, dragEndEvent);",
            source, target)

    @allure.step('Получаем каунтер добавленных ингредиентов')
    def get_counter_of_ingredients_in_basket(self):
        return self.get_text_from_element(HomePageLocators.COUNTER_INGREDIENT_IN_BASKET)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_modal_window_after_create_order(self):
        self.find_element_with_wait(HomePageLocators.MODAL_WINDOW_AFTER_CREATE_ORDER)
        return self.check_displaying_of_element(HomePageLocators.MODAL_WINDOW_AFTER_CREATE_ORDER)

    @allure.step("Закрытие окна заказа")
    def close_order_window(self):
        close_button = self.find_element_with_wait(HomePageLocators.CLOSE_MOD_WINDOW_AFTER_CREATE_ORDER)
        self.click_on_element_js(close_button)

    @allure.step('Получить номер заказа в модальном окне после создания заказа')
    def get_number_in_modal_window_after_create_order(self):
        self.wait_for_element_to_change_text(HomePageLocators.MODAL_NEW_ORDER_NUMBER, '9999')
        return self.get_text_from_element(HomePageLocators.MODAL_NEW_ORDER_NUMBER)
