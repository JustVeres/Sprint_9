import allure
from data.data_urls import RECIPES_CREATE_URL
from data.data_page import RecipesCreatePageData as RCPD
from pages.base_page import BasePage
from locators import RecipesCreatePageLocators as RCPL
from helpers import RecipesCreatePageHelpers as RCPH

class RecipesCreatePage(BasePage):

    @allure.step('Ожидаем загрузки страницы /recipes/create')
    def wait_url_recipes_create_page(self):
        self.wait_url(RECIPES_CREATE_URL)

    @allure.step('Заполняем поле «Название рецепта»')
    def input_recipe_name(self):
        self.input_text(RCPL.RECIPE_NAME_FIELD, RCPD.recipe_name)

    @allure.step('Деактивируем чекбокс «Обед»')
    def deactivate_checkbox_lunch(self):
        self.click(RCPL.LUNCH_CHECKBOX)

    @allure.step('Деактивируем чекбокс «Ужин»')
    def deactivate_checkbox_dinner(self):
        self.click(RCPL.DINNER_CHECKBOX)

    @allure.step('Заполняем поле «Ингредиенты» с названием')
    def input_ingredients_name(self):
        self.input_text(RCPL.INGREDIENT_NAME, RCPD.ingredients_name)

    @allure.step('Выбираем ингредиент из списка по названию')
    def select_ingredient(self):
        self.wait_visible(RCPL.INGREDIENT_SUGGESTIONS)
        name = self.wait_visible_return(RCPH.ingredient_option_by_name(RCPD.ingredients_name))
        name.click()

    @allure.step('Заполняем поле «Ингредиенты» с весом')
    def input_ingredients_weight(self):
        self.input_text(RCPL.INGREDIENT_AMOUNT, RCPD.ingredients_weight)

    @allure.step("Нажимаем кнопку «Добавить ингредиент»")
    def click_add_ingredient(self):
        self.wait_visible(RCPL.ADD_INGREDIENT_BUTTON)
        self.click(RCPL.ADD_INGREDIENT_BUTTON)

    @allure.step("Заполняем поле «Время приготовления»")
    def input_cooking_time(self,):
        self.input_text(RCPL.COOKING_TIME_FIELD, RCPD.cooking_time)

    @allure.step("Заполняем поле «Описание рецепта»")
    def input_recipe_description(self):
        self.input_text(RCPL.DESCRIPTION_FIELD, RCPD.recipe_description)

    @allure.step("Загружаем фото рецепта")
    def upload_photo_recipe(self):
        self.upload_photo(RCPD.recipe_photo, RCPL.UPLOAD_PHOTO_BUTTON)

    @allure.step("Нажимаем кнопку «Создать рецепт»")
    def click_create_recipe_button(self):
        self.click(RCPL.CREATE_RECIPE_BUTTON_ENABLE)
