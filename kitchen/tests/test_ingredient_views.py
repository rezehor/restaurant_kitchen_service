from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Ingredient

INGREDIENT_URL = reverse("kitchen:ingredient-list")


class PublicIngredientTest(TestCase):
    def test_login_required(self):
        res = self.client.get(INGREDIENT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateIngredientTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test12345",
        )
        self.client.force_login(self.user)

    def test_retrieve_ingredient(self):
        Ingredient.objects.create(name="Avocado")
        Ingredient.objects.create(name="Beans")
        response = self.client.get(INGREDIENT_URL)
        self.assertEqual(response.status_code, 200)
        ingredient = Ingredient.objects.all()
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredient),
        )
        self.assertTemplateUsed(response, "kitchen/ingredient_list.html")
