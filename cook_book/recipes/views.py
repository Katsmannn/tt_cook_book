from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db import transaction
from django.db.models import F

from .models import Recipe, Product, RecipesProduct


@transaction.atomic
def add_product_to_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    product = get_object_or_404(Product, pk=request.GET.get('product_id'))
    obj, _ = RecipesProduct.objects.update_or_create(
        recipe=recipe, product=product,
        defaults={'weight': request.GET.get('weight')},
    )
    return HttpResponse(f'{obj} - {obj.weight}')


@transaction.atomic
def cook_recipe(request, recipe_id):
    Product.objects.filter(recipe__pk=recipe_id).update(cook=F('cook') + 1)
    return HttpResponse('OK')


def show_recipes_without_product(request, product_id):
    recipes = Recipe.objects.exclude(
        pk__in=Recipe.objects.filter(
            products__pk=product_id, recipesproduct__weight__gte=10
        ).values_list('pk')
    )
    product_name = Product.objects.get(pk=product_id).name

    return render(
        request, 'recipe_without_product.html', context={
            "recipes": recipes, 'product_name': product_name
        }
    )
