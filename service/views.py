from django.contrib.auth.mixins import LoginRequiredMixin
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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = Dishtype
    paginate_by = 6
    template_name = "service/dishtype_list.html"
    ordering = ("name" ,)


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dishtype
    fields = "__all__"
    success_url = reverse_lazy("service:dishtype-list")
    template_name = "service/dishtype_create.html"

class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dishtype
    success_url = reverse_lazy("service:dishtype-list")
    template_name = "service/dishtype_delete.html"


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dishtype
    template_name = "service/dishtype_detail.html"

class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 6
    template_name = "service/dish_list.html"
    ordering = ("name" ,)


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "service/dish_detail.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("service:dish-list")
    template_name = "service/dish_form.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("service:dish-list")
    template_name = "service/dish_form.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("service:dish-list")
    template_name = "service/dish_delete.html"


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 6
    template_name = "service/ingredient_list.html"
    ordering = ("name" ,)


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("service:ingredient-list")
    template_name = "service/ingredient_create.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 6
    template_name = "service/cook_list.html"
    ordering = ("username", )


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "years_of_experience")
    success_url = reverse_lazy("service_url:cook-list")
    template_name = "service/cook_form.html"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "service/cook_detail.html"


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("service:cook-list")
    template_name = "service/cook_delete.html"


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "years_of_experience")
    success_url = reverse_lazy("service:cook-list")
    template_name = "service/cook_form.html"

