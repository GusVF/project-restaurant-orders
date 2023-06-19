import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.data = []
        self.source_path = source_path
        self.read_file_csv()
        self.create_dishes()

    def read_file_csv(self):
        with open(self.source_path, encoding="utf8") as file:
            recipes = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = recipes
        self.data = data

    def create_dishes(self):
        counter = ""
        for recipe in self.data:
            if recipe[0] != counter:
                print(recipe[0], counter)
                counter = recipe[0]
                new_recipe = Dish(recipe[0], float(recipe[1]))
                new_recipe.add_ingredient_dependency(
                    Ingredient(recipe[2]), int(recipe[3])
                )
                self.dishes.add(new_recipe)
            else:
                dish = list(self.dishes)[0]
                if dish.name != recipe[0]:
                    dish = list(self.dishes)[1]
                dish.add_ingredient_dependency(
                    Ingredient(recipe[2]), int(recipe[3])
                )
        return self.dishes
