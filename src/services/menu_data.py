import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.menu_data(source_path)

    def menu_data(self, source_path: str):
        with open(source_path, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                dish_name, price, ingredient_name, quantity = row
                self._add_dish_ingredient(
                    dish_name, float(price), ingredient_name, int(quantity)
                )

    def _add_dish_ingredient(
        self, dish_name: str, price: float, ingredient_name: str, quantity: int
    ):
        dish = self._get_create_dish(dish_name, price)
        ingredient = self._get_create_ingredient(ingredient_name)
        dish.add_ingredient_dependency(ingredient, quantity)

    def _get_create_dish(self, dish_name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == dish_name and dish.price == price:
                return dish
        new_dish = Dish(dish_name, price)
        self.dishes.add(new_dish)
        return new_dish

    def _get_create_ingredient(self, ingredient_name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_name:
                return ingredient
        new_ingredient = Ingredient(ingredient_name)
        self.ingredients.add(new_ingredient)
        return new_ingredient
