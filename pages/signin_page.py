import allure
from data.data_urls import SIGNIN_URL
from locators import SigninPageLocators as SIPL
from pages.base_page import BasePage

class SigninPage(BasePage):

    @allure.step('Ожидаем загрузки страницы /signin')
    def wait_url_signin_page(self):
        self.wait_url(SIGNIN_URL)

    @allure.step('Ожидаем видимости поля «Электронная почта»')
    def wait_email_field_visible(self):
        self.wait_visible(SIPL.EMAIL_FIELD)
        return True

    @allure.step('Ожидаем видимости поля «Пароль»')
    def wait_password_field_visible(self):
        self.wait_visible(SIPL.PASSWORD_FIELD)
        return True

    @allure.step('Ожидаем видимости неактивной кнопки «Войти»')
    def wait_login_button_disabled_visible(self):
        return self.wait_element_text(SIPL.LOGIN_BUTTON_DISABLED)

    @allure.step('Ожидаем видимости заголовка «Войти на сайт»')
    def wait_login_title_visible(self):
        return self.wait_element_text(SIPL.LOGIN_PAGE_TITLE)

    @allure.step('Заполняем поле «Электронная почта')
    def input_email(self, email):
        self.input_text(SIPL.EMAIL_FIELD, email)

    @allure.step('Заполняем поле «Пароль»')
    def input_password(self, password):
        self.input_text(SIPL.PASSWORD_FIELD, password)

    @allure.step('Кликаем по кнопке «Войти» на странице')
    def click_login_on_page(self):
        self.click(SIPL.LOGIN_BUTTON_ENABLED)
