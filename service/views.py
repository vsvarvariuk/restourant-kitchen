from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from service.models import (Ingredient,
                            Dishtype,
                            Dish,
                            Cook)


def index(request: HttpRequest) -> HttpResponse:
    ingredient = Ingredient.objects.count()
    dish_type = Dishtype.objects.count()
    dish = Dish.objects.count()
    cooks = Cook.objects.count()
    context = {
        "ingredient": ingredient,
        "dish_type": dish_type,
        "dish": dish,
        "cooks": cooks
    }
    return render(request, "service/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = Dishtype
    paginate_by = 7
    template_name = "service/dishtype_list.html"


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 7
    template_name = "service/dish_list.html"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "service/dish_detail.html"


class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 7
    template_name = "service/ingredient_list.html"


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 7
    template_name = "service/cook_list.html"


class CookCreateView(generic.CreateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "years_of_experience")
    success_url = reverse_lazy("service_url:cook-list")
    template_name = "service/cook_create.html"


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "service/cook_detail.html"




