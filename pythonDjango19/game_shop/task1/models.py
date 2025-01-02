from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=6)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(decimal_places=2, max_digits=4)
    size = models.DecimalField(decimal_places=3, max_digits=5)
    description = models.TextField()
    age_limited = models.BooleanField(default=False, help_text='Age = 18+')
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title
