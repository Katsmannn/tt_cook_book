from django.contrib import admin

from .models import Recipe, Product, RecipesProduct


@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipesProduct)
class RecipesProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight')

    def name(self, obj):
        return f'{obj.recipe} - {obj.product}'
