from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType

DISH_TYPE_URL = reverse("kitchen:dish-types-list")

class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        DishType.objects.create(name="Breakfast")
        DishType.objects.create(name="Dessert")
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_type = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_type),
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")