from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"

    def __str__(self):
        return self.username


class Dishtype(models.Model):
    name = models.CharField(max_length=65, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=65)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(Dishtype, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook)

    class Meta:
        unique_together = ['name', 'dish_type']

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=65, unique=True)
    dish = models.ManyToManyField(Dish)

    def __str__(self):
        return self.name
