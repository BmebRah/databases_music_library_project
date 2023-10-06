from lib.recipe import *

def test_it_constructs_correctly():
    recipe = Recipe(1, 'pasta', 30, 1)
    assert recipe.id == 1
    assert recipe.name == 'pasta'
    assert recipe.cooking_time == 30
    assert recipe.rating == 1

def test_formats_correctly():
    recipe = Recipe(1, "pasta", 30, 1)
    assert str(recipe) == "Recipe(1, pasta , 30, 1)"

def test_recipes_are_equal():
    recipe1 = Recipe(1, "pasta", 30, 1)
    recipe2 = Recipe(1, "pasta", 30, 1)
    assert recipe1 ==recipe2