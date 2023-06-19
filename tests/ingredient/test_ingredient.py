from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("farinha")
    ingredient_2 = Ingredient("farinha")
    ingredient_3 = Ingredient("presunto")

    assert ingredient_1.name == "farinha"

    ingredient_restrictions = {
        Restriction.GLUTEN
    }
# Testing ingredient restricitons and name match
    assert ingredient_1.restrictions == ingredient_restrictions
    assert ingredient_3.restrictions != ingredient_restrictions
#   Testing __repr__
    assert repr(ingredient_1) == "Ingredient('farinha')"

#   Testing __eq__
    assert ingredient_1 == ingredient_2
    assert ingredient_1 != ingredient_3

# Testing __hash__
    assert hash(ingredient_1) == hash(ingredient_2)
    assert hash(ingredient_1) != hash(ingredient_3)
