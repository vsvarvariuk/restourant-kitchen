from django.urls import path
from .views import (index,
                    DishTypeListView,
                    DishListView,
                    IngredientListView,
                    CookListView)

urlpatterns = [
   path("", index, name="index"),
   path("dishtype/", DishTypeListView.as_view(), name="dishtype-list"),
   path("dish/", DishListView.as_view(), name="dish-list"),
   path("ingredient/", IngredientListView.as_view(), name="ingredient-list"),
   path("cooks/", CookListView.as_view(), name="cook-list"),

]

app_name = "service"