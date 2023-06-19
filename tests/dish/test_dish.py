from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    # Tests dish attributes name, price, recipe
    dish_1 = Dish("lasanha presunto", 25.90)
    same_dish = Dish("lasanha presunto", 25.90)
    other_dish = Dish("lasanha beringela", 27.00)

    assert dish_1.name == "lasanha presunto"
    assert dish_1.price == 25.90
    assert dish_1.recipe == {}

    # Tests __repr__
    assert repr(dish_1) == "Dish('lasanha presunto', R$25.90)"

    # Tests dish __hash__ in True and False instances
    assert hash(dish_1) == hash(same_dish)

    assert hash(dish_1) != hash(other_dish)

    # Tests __eq__
    assert dish_1 == same_dish
    assert dish_1 != other_dish

    # Tests dish invalid price type
    with pytest.raises(TypeError):
        Dish("lasanha presunto", "25.90")

    # Tests dish invalid price value
    with pytest.raises(ValueError):
        Dish("lasanha presunto", -25.90)

    # Tests adding Ingredients
    ingredient_1 = Ingredient("sal")
    ingredient_2 = Ingredient("agua")

    dish_1.add_ingredient_dependency(ingredient_1, 5)
    dish_1.add_ingredient_dependency(ingredient_2, 10)

    assert dish_1.recipe.get(ingredient_1) == 5
    assert dish_1.recipe.get(ingredient_2) == 10

    # Tests Dish get_ingredients
    ingredients = dish_1.get_ingredients()

    assert len(ingredients) == 2
    assert ingredient_1 in ingredients
    assert ingredient_2 in ingredients

    # Tests Dish restrictions
    assert list(dish_1.get_restrictions()) == []
