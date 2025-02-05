import pytest
import allure
from utils.helper import *
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.param
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
@allure.title('Создание и удаление тестового пользователя')
def create_and_delete_user():
    payload, response = auth_user_and_get_creds()
    email = payload.get('email')
    password = payload.get('password')
    yield email, password
    access_token = response.json().get('accessToken')
    requests.delete(f'{URLs.BASE_URL}{URLs.DELETE_USER_URL}', headers={'Authorization': access_token})
