from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

COOK_URL = reverse("kitchen:cook-list")


class PublicCookTest(TestCase):
    def test_login_required(self):
        res = self.client.get(COOK_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test12345",
        )
        self.client.force_login(self.user)

    def test_create_cook(self):
        form_data = {
            "username": "new_user",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "new_first_name",
            "last_name": "new_last_name",
            "years_of_experience": 5,
        }
        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(
            new_user.years_of_experience,
            form_data["years_of_experience"],
        )
