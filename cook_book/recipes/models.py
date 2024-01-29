from django.db import models


class Product(models.Model):

    name = models.CharField(
        verbose_name='name',
        max_length=150
    )
    cook = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):

    name = models.CharField(
        max_length=150
    )
    products = models.ManyToManyField(
        to=Product,
        through='RecipesProduct'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class RecipesProduct(models.Model):

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product'
    )
    weight = models.PositiveSmallIntegerField()
