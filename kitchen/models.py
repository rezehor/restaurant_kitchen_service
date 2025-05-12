from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return (f"{self.username} ({self.first_name} {self.last_name})"
                f" exp.{self.years_of_experience}")

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes"
    )
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - (dish type: {self.dish_type.name})"
