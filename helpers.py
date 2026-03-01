import random
import string
from selenium.webdriver.common.by import By

class BasePageHelpers:
    def random_string(length=8): # Генерируем случайные буквы
        return ''.join(random.choices(string.ascii_lowercase, k=length))

class RecipesCreatePageHelpers:
    def ingredient_option_by_name(self: str): # Динамический локатор для выбора ингедиента из списка
        return By.XPATH, f"//div[contains(@class,'styles_container')]//div[normalize-space()='{self}']"
