from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType

DISH_URL = reverse("kitchen:dish-list")

class PublicDishTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish(self):
        dish_type = DishType.objects.create(name="Main Course")
        Dish.objects.create(
            name="BBQ Ribs",
            description="Slow-cooked pork ribs glazed with smoky barbecue sauce.",
            price=10,
            dish_type=dish_type,
        )
        Dish.objects.create(
            name="Beef Stroganoff",
            description="Tender beef slices in a creamy mushroom sauce served over noodles.",
            price=15,
            dish_type=dish_type,
        )
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dish = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dish),
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")