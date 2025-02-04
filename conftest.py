import pytest
import allure
from utils.helper import *
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
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
