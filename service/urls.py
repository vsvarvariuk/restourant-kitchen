from django.urls import path
from .views import (index,
                    DishTypeListView,
                    DishListView)

urlpatterns = [
   path("", index, name="index"),
   path("dishtype/", DishTypeListView.as_view(), name="dishtype-list"),
   path("dish/", DishListView.as_view(), name="dish-list")
]

app_name = "service"