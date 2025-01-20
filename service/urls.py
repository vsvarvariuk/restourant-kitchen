from django.urls import path
from .views import (index,
                    DishTypeListView,
                    DishListView,
                    DishDetailView,
                    DishUpdateView,
                    DishCreateView,
                    IngredientListView,
                    CookListView,
                    CookCreateView,
                    CookDeleteView,
                    CookUpdateView,
                    CookDetailView)

urlpatterns = [
   path("", index, name="index"),
   path("dishtype/", DishTypeListView.as_view(), name="dishtype-list"),
   path("dish/", DishListView.as_view(), name="dish-list"),
   path("dish-detail/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
   path("dish-update/<int:pk>/", DishUpdateView.as_view(), name="dish-update"),
   path("dish-create/", DishCreateView.as_view(), name="dish-create"),
   path("ingredient/", IngredientListView.as_view(), name="ingredient-list"),
   path("cooks/", CookListView.as_view(), name="cook-list"),
   path("cooks-create/", CookCreateView.as_view(), name="cook-create"),
   path("cooks-update/<int:pk>", CookUpdateView.as_view(), name="cook-update"),
   path("cooks-delete/<int:pk>/", CookDeleteView.as_view(), name="cook-delete"),
   path("cooks-detail/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),

]

app_name = "service"