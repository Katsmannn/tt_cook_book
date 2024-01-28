from django.db import models


class Ingredient(models.Model):

    name = models.CharField(
        verbose_name='name',
        max_length=150
    )
    uses = models.PositiveIntegerField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):

    name = models.CharField(
        max_length=150
    )
    ingredients = models.ManyToManyField(
        to=Ingredient,
        through='RecipesIngredient'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class RecipesIngredient(models.Model):

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE
    )
    amount = models.PositiveSmallIntegerField()
