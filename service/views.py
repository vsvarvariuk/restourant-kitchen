from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
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
    paginate_by = 5
    template_name = "service/dishtype_list.html"


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    template_name = "service/dish_list.html"




