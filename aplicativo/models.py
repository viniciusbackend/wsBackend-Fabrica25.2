import requests
from django.db import models
class Nutricao(models.Model):
    calories = models.CharField(max_length=155)
    fat = models.CharField(max_length=155)
    sugar = models.CharField(max_length=155)
    carbohydrates = models.CharField(max_length=155)
    protein = models.CharField(max_length=155)

    def __str__(self):
        return self.calories

class Fruta(models.Model):
    name = models.CharField(max_length=155, unique=True)
    family = models.CharField(max_length=155)
    genus = models.CharField(max_length=155)
    nutritions = models.ForeignKey(Nutricao, on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.name