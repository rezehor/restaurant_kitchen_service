from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Ingredient, Dish


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
            years_of_experience=10,
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
            f" exp.{cook.years_of_experience}"
        )

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="test")
        self.assertEqual(str(ingredient), ingredient.name)

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="test")
        dish = Dish.objects.create(
            name="test",
            description="test",
            price=10,
            dish_type=dish_type,
        )
        self.assertEqual(
            str(dish),
            f"{dish.name} - (dish type: {dish.dish_type.name})"
        )

    def test_create_cook_with_years_of_experience(self):
        username = "test"
        password = "test123"
        years_of_experience = 20
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))
