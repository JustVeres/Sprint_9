import allure
from pages.base_page import BasePage
from locators import SignupPageLocators as SUPL

class SignupPage(BasePage):

    @allure.step('Заполняем поле «Имя»')
    def input_first_name(self, first_name):
        self.input_text(SUPL.FIRST_NAME_FIELD, first_name)

    @allure.step('Заполняем поле «Фамилия»')
    def input_last_name(self, last_name):
        self.input_text(SUPL.LAST_NAME_FIELD, last_name)

    @allure.step('Заполняем поле «Имя пользователя»')
    def input_nickname(self, nickname):
        self.input_text(SUPL.NICKNAME_FIELD, nickname)

    @allure.step('Заполняем поле «Адрес электронной почты»')
    def input_email(self, email):
        self.input_text(SUPL.EMAIL_FIELD, email)

    @allure.step('Заполняем поле «Пароль»')
    def input_password(self, password):
        self.input_text(SUPL.PASSWORD_FIELD, password)

    @allure.step('Нажимаем на кнопку «Создать аккаунт» на странице')
    def click_create_account_on_page(self):
        self.click(SUPL.CREATE_ACCOUNT_BUTTON_ENABLED)
