from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import DishType, Dish, Cook, Ingredient


def index(request):
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_ingredients = Ingredient.objects.count()

    context = {
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients,
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeDetailView(generic.DetailView):
    model = DishType


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 10


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 10


class IngredientCreateView(generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientUpdateView(generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDeleteView(generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")


class CookListView(generic.ListView):
    model = Cook


class CookDetailView(generic.DetailView):
    model = Cook


class CookCreateView(generic.CreateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


