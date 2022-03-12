from django.db import models
from shared_app.models import Category


class Food(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, related_name="foods", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
