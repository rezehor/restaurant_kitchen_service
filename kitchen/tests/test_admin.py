from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Cook


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = Cook.objects.create_superuser(
            username="admin",
            password="testadmin"
        )
        self.client.force_login(self.admin_user)
        self.cook = Cook.objects.create_superuser(
            username="driver",
            password="testdriver",
            years_of_experience=10,
        )

    def test_cook_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detail_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)
