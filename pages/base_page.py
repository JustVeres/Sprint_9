import allure
import os
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators as BPL
from data.data_urls import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step('Открыть сайт foodgram')
    def open_main_page(self):
        self.open(BASE_URL)

    """Хедеры"""
    @allure.step('Клик по «Создать аккаунт» в хедере')
    def click_create_account_on_header(self):
        self.click(BPL.CREATE_ACCOUNT_HEADER)

    @allure.step('Клик по «Войти» в хедере')
    def click_login_on_header(self):
        self.click(BPL.SIGNIN_HEADER)

    """Вспомогательные методы"""
    """Действие: открыть/кликнуть/выбрать/ввести/вернуть etc."""

    @allure.step('Открыть URL')
    def open(self, url):
        self.driver.get(url)

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Кликаем на элемент')
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.execute_script("arguments[0].click();", element)

    @allure.step('Вводим текст в поле')
    def input_text(self, locator, text):
        element = self.wait_visible_return(locator)
        element.send_keys(text)

    @allure.step("Загружаем фото")
    def upload_photo(self, path, locator):
        file_path = os.path.abspath(path)
        upload_input = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].style.display='block';", upload_input)
        upload_input.send_keys(file_path)


    """Ожидание: видимость/исчезновение"""

    @allure.step('Ожидаем URL')
    def wait_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step('Ожидаем и возвращаем видимый элемент')
    def wait_visible_return(self, locator): #
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание видимости элемента')
    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем видимость элемента и возвращаем текст')
    def wait_element_text(self, locator):
        self.wait_visible(locator)
        return self.driver.find_element(*locator).text

    """Скрипты"""

    @allure.step("Выполнение JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
