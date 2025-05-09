from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-types-create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-types-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-types-delete"),
]

app_name = "kitchen"