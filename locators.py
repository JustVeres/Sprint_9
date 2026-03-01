from selenium.webdriver.common.by import By

class BasePageLocators:
    CREATE_ACCOUNT_HEADER = (By.XPATH, "//a[text()='Создать аккаунт' and @href='/signup']")
    SIGNIN_HEADER = (By.LINK_TEXT, "Войти")

class SignupPageLocators:
    FIRST_NAME_FIELD = (By.NAME, "first_name")
    LAST_NAME_FIELD = (By.NAME, "last_name")
    NICKNAME_FIELD = (By.NAME, "username")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    CREATE_ACCOUNT_BUTTON_ENABLED = (By.XPATH, "//button[normalize-space()='Создать аккаунт' and not(@disabled)]")

class SigninPageLocators:
    LOGIN_PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Войти на сайт']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON_DISABLED = (By.XPATH, "//button[normalize-space()='Войти' and @disabled]")
    LOGIN_BUTTON_ENABLED = (By.XPATH, "//button[normalize-space()='Войти' and not(@disabled)]")

class RecipesPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//header//a[normalize-space()='Выход']")
    CREATE_RECIPE_HEADER = (By.XPATH, "//a[normalize-space()='Создать рецепт']")
    RECIPE_CARD_TITLE = (By.CSS_SELECTOR, "h1.styles_single-card__title__2QMPq")
    RECIPE_CARD_IMAGE = (By.CSS_SELECTOR, "img.styles_single-card__image__O135K")

class RecipesCreatePageLocators:
    RECIPE_NAME_FIELD = (By.XPATH, "//div[normalize-space()='Название рецепта']/following::input[1]")
    LUNCH_CHECKBOX = (By.XPATH, "//span[normalize-space()='Обед']/preceding-sibling::button")
    DINNER_CHECKBOX = (By.XPATH, "//span[normalize-space()='Ужин']/preceding-sibling::button")
    INGREDIENT_NAME = (By.XPATH, "//div[normalize-space()='Ингредиенты']/ancestor::*[1]//input[contains(@class,'ingredientsInput')]")
    INGREDIENT_SUGGESTIONS = (By.CSS_SELECTOR, "div.styles_container__3ukwm")
    INGREDIENT_AMOUNT = (By.XPATH, "//div[normalize-space()='Ингредиенты']/ancestor::*[1]//input[contains(@class,'ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[normalize-space()='Добавить ингредиент']")
    COOKING_TIME_FIELD = (By.XPATH, "//label[.//div[normalize-space()='Время приготовления']]//input")
    DESCRIPTION_FIELD = (By.XPATH, "//label[.//div[normalize-space()='Описание рецепта']]//textarea")
    UPLOAD_PHOTO_BUTTON = (By.XPATH, "//input[@type='file']")
    CREATE_RECIPE_BUTTON_ENABLE = (By.XPATH, "//button[text()='Создать рецепт']")
