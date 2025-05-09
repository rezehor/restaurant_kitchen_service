from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-types-detail"),

    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-types-create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-types-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-types-delete"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("ingredient/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredient/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredient/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredient/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient-delete"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cook/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
]

app_name = "kitchen"