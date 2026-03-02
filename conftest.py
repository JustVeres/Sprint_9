import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers import BasePageHelpers
from pages.base_page import BasePage
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage
from pages.recipes_page import RecipesPage
from pages.recipes_create_page import RecipesCreatePage

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    selenoid_url = os.getenv(
        "SELENOID_URI",
        "http://selenoid:4444/wd/hub"
    )

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True,
            "enableVideo": False
        }
    )
    driver = webdriver.Remote(command_executor=selenoid_url, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def driver3():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def open_main_page(base_page):
    base_page.open_main_page()

@pytest.fixture
def create_account():
    """Фикстура для генерации данных нового аккаунта"""
    nickname = BasePageHelpers.random_string()
    email = f"{BasePageHelpers.random_string()}@yandex.ru"
    password = BasePageHelpers.random_string()
    return {
        "first_name": "Gordon",
        "last_name": "Freeman",
        "nickname": nickname,
        "email": email,
        "password": password
    }

@pytest.fixture
def create_account_and_authorization(base_page, signup_page, signin_page, create_account):
    """Фикстура, которая регистрирует аккаунт и возвращает данные для входа"""
    # 1. Предусловие для регистрации через UI
    base_page.open_main_page()
    base_page.click_create_account_on_header()

    signup_page.input_first_name(create_account["first_name"])
    signup_page.input_last_name(create_account["last_name"])
    signup_page.input_nickname(create_account["nickname"])
    signup_page.input_email(create_account["email"])
    signup_page.input_password(create_account["password"])
    signup_page.click_create_account_on_page()
    signin_page.wait_url_signin_page()

    # 2. Возвращаем nickname и password для последующей авторизации
    return {
        "nickname": create_account["nickname"],
        "password": create_account["password"]
    }

@pytest.fixture
def authorization(create_account_and_authorization, signin_page, recipes_page):
    """Фикстура для авторизации"""
    signin_page.input_email(create_account_and_authorization["nickname"])
    signin_page.input_password(create_account_and_authorization["password"])
    signin_page.click_login_on_page()
    recipes_page.wait_url_recipes_page()

"""Фикстуры для страниц"""
@pytest.fixture
def base_page(driver):
    base_page = BasePage(driver)
    return base_page

@pytest.fixture
def signup_page(driver):
    signup_page = SignupPage(driver)
    return signup_page

@pytest.fixture
def signin_page(driver):
    signin_page = SigninPage(driver)
    return signin_page

@pytest.fixture
def recipes_page(driver):
    recipes_page = RecipesPage(driver)
    return recipes_page

@pytest.fixture
def recipes_create_page(driver):
    recipes_create_page = RecipesCreatePage(driver)
    return recipes_create_page
