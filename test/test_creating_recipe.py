import allure
from data.data_page import RecipesCreatePageData as RCPD

class TestCreatingRecipe:

    @allure.title('Создание рецепта')
    def test_create_recipes(self, authorization, recipes_page, recipes_create_page):

        with allure.step("Авторизоваться и перейти на таб «Создать рецепт»"):
            recipes_page.click_create_recipe_on_header()
            recipes_create_page.wait_url_recipes_create_page()

        with allure.step("Заполнить все поля формы создания рецепта и нажать кнопку «Создать рецепт»"):
            recipes_create_page.input_recipe_name()
            recipes_create_page.deactivate_checkbox_lunch()
            recipes_create_page.deactivate_checkbox_dinner()
            recipes_create_page.input_ingredients_name()
            recipes_create_page.select_ingredient()
            recipes_create_page.input_ingredients_weight()
            recipes_create_page.click_add_ingredient()
            recipes_create_page.input_cooking_time()
            recipes_create_page.input_recipe_description()
            recipes_create_page.upload_photo_recipe()
            recipes_create_page.click_create_recipe_button()

        with allure.step("Проверить, отображается ли: карточка созданного рецепта"):
            assert recipes_page.is_recipe_image_visible()

        with allure.step("Проверить, отображается ли: название, которое заполняли при создании"):
            assert recipes_page.get_recipe_title() == RCPD.recipe_name
