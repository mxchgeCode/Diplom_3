import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.time = 10

    @allure.step('Подождать загрузку элемента')
    def find_element_with_wait(self, locator):
        return (WebDriverWait(self.driver, self.time).
                until(expected_conditions.visibility_of_element_located(locator)))

    @allure.step('Кликнуть на элемент')
    def click_to_element(self, locator):
        element = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(element).click().perform()

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, from_element, to_element):
        ActionChains(self.driver).drag_and_drop(from_element, to_element).pause(5).perform()

    @allure.step('Проверить ,что элемент кликабелен')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, self.time).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Подождать закрытие элемента')
    def wait_closing_element(self, locator):
        WebDriverWait(self.driver, self.time).until_not(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Добавить текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получить текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Подождать смену текста на элементе')
    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(self.driver, self.time).until_not(expected_conditions.
                                                               text_to_be_present_in_element(locator, value))

    def click_on_element_js(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)

    def find_element_with_wait_overlay(self, locator):
        WebDriverWait(self.driver, self.time).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
