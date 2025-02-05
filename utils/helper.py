import requests
from data import URLs


def create_random_creds():
    email = 'jessica@example.org'
    password = 'jessicaexample'
    name = 'jessica'
    reg_data = {
        "email": email,
        "password": password,
        "name": name,
    }
    return reg_data


def auth_user_and_get_creds():
    payload = create_random_creds()
    response = requests.post(f'{URLs.BASE_URL}{URLs.CREATE_USER_URL}', json=payload)
    return payload, response


def get_access_token(response):
    return response.json().get('accessToken')


def prepare_data(create_and_delete_user, driver, AccountPage=None, OrderFeedPage=None, HomePage=None):
    email, password = create_and_delete_user
    account_page = AccountPage(driver)
    feed_page = OrderFeedPage(driver)
    home_page = HomePage(driver)
    return email, password, account_page, feed_page, home_page
