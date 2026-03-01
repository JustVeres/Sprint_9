import allure
from pages.base_page import BasePage
from data.data_urls import RECIPES_URL
from locators import RecipesPageLocators as RPL

class RecipesPage(BasePage):

    @allure.step('Ожидаем загрузки страницы /recipes')
    def wait_url_recipes_page(self):
        self.wait_url(RECIPES_URL)

    @allure.step('Ожидаем видимости кнопки «Выход» в хедере')
    def wait_logout_button_visible(self):
        return self.wait_element_text(RPL.LOGOUT_BUTTON)

    @allure.step('Клик по «Создать рецепт» в хедере')
    def click_create_recipe_on_header(self):
        self.click(RPL.CREATE_RECIPE_HEADER)

    @allure.step("Получаем название созданного рецепта")
    def get_recipe_title(self):
        element = self.wait_visible_return(RPL.RECIPE_CARD_TITLE)
        return element.text

    @allure.step("Проверяем, отображается ли изображение рецепта")
    def is_recipe_image_visible(self):
        element = self.wait_visible_return(RPL.RECIPE_CARD_IMAGE)
        return element.is_displayed() and bool(element.get_attribute("src"))
