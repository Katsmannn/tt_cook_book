from django.urls import path

from . import views


urlpatterns = [
    path('recipes/<int:recipe_id>/edit/', views.add_product_to_recipe,
         name='edit_recipe'),
    path('recipes/<int:recipe_id>/cook', views.cook_recipe,
         name='cook_recipe'),
    path(
        'recipes/without_product/<int:product_id>',
        views.show_recipes_without_product,
        name='without_product'
    ),
]
