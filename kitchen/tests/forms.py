from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, Ingredient, Dish, DishType


class SearchFormTests(TestCase):
    def setUp(self):
        user = Cook.objects.create_user(
            username="test",
            password="test123",
            years_of_experience=5,
        )
        self.client.force_login(user)

    def test_search_form_in_ingredient_list(self):
        Ingredient.objects.create(name="test")
        ingredient = Ingredient.objects.filter(name__icontains="t")

        url = reverse("kitchen:ingredient-list") + "?name=t"
        response = self.client.get(url)
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredient),
        )

    def test_search_form_in_dish_list(self):
        dish_type = DishType.objects.create(name="Main Course")
        Dish.objects.create(
            name="BBQ Ribs",
            description="Slow-cooked pork ribs glazed with smoky barbecue sauce.",
            price=10,
            dish_type=dish_type,
        )
        dish = Dish.objects.filter(name__icontains="i")

        url = reverse("kitchen:dish-list") + "?name=i"
        response = self.client.get(url)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dish),
        )