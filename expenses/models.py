from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    data = models.DateField()
