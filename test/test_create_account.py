import allure
from data.data_urls import SIGNIN_URL

class TestCreateAccount:

    @allure.title('Создание аккаунта')
    def test_open_authorization_page_after_create_account(self, open_main_page, create_account, base_page, signup_page, signin_page):

        with allure.step("Нажать кнопку «Создать аккаунт»"):
            base_page.click_create_account_on_header()

        with allure.step("Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»"):
            signup_page.input_first_name(create_account["first_name"])
            signup_page.input_last_name(create_account["last_name"])
            signup_page.input_nickname(create_account["nickname"])
            signup_page.input_email(create_account["email"])
            signup_page.input_password(create_account["password"])
            signup_page.click_create_account_on_page()

        with allure.step("Проверить: Произошёл ли переход на страницу авторизации"):
            signin_page.wait_url_signin_page()
            assert signin_page.get_current_url() == SIGNIN_URL

        with allure.step("Проверить: отображается ли форма авторизации"):
            assert signin_page.wait_login_title_visible() == 'Войти на сайт'
            assert signin_page.wait_email_field_visible()
            assert signin_page.wait_password_field_visible()
            assert signin_page.wait_login_button_disabled_visible() == 'Войти'
