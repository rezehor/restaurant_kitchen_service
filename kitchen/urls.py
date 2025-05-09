from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
]

app_name = "kitchen"