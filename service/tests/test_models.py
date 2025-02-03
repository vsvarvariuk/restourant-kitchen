from django.contrib.auth import get_user_model
from django.test import TestCase

from service.models import Dish, Dishtype, Ingredient


class ModelsTest(TestCase):
    def test_cook(self):
        cook = get_user_model().objects.create_user(
            years_of_experience=1,
            username="Roman_vis",
            first_name="Roman",
            last_name="Vistov")
        self.assertEqual(str(cook), "Roman_vis")
        self.assertEqual(cook.years_of_experience, 1)

    def test_dishtype_str(self):
        dish_type = Dishtype.objects.create(name="drinks")
        self.assertEqual(str(dish_type), "drinks")

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="Tomato")
        self.assertEqual(str(ingredient), "Tomato")

    def test_dish_str(self):
        dishtype = Dishtype.objects.create(name="Main Course")
        dish = Dish.objects.create(name="Grilled Chicken",
                                   description="Delicious grilled chicken",
                                   price=15.99,
                                   dish_type=dishtype)
        self.assertEqual(str(dish), "Grilled Chicken")
