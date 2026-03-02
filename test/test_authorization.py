import allure
from data.data_urls import RECIPES_URL

class TestAuthorization:

    @allure.title('Авторизация')
    def test_open_main_page_after_authorization(self, open_main_page, create_account_and_authorization, base_page, signin_page, recipes_page):
        with allure.step('Нажать кнопку «Войти»'):
            base_page.click_login_on_header()
            signin_page.wait_url_signin_page()

        with allure.step('Заполнить все поля формы авторизации и нажать кнопку «Войти»'):
            signin_page.input_email(create_account_and_authorization["nickname"])
            signin_page.input_password(create_account_and_authorization["password"])
            signin_page.click_login_on_page()

        with allure.step('Проверить: Произошёл ли переход на главную страницу'):
            recipes_page.wait_url_recipes_page()
            assert recipes_page.get_current_url() == RECIPES_URL

        with allure.step('Проверить: отображается ли кнопка «Выход»'):
            assert recipes_page.wait_logout_button_visible() == "Выход"
