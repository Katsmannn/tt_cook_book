import csv
from django.core.management.base import BaseCommand, CommandError
from recipes.models import Ingredient, Recipe


class Command(BaseCommand):
    help = "Create data in db"

    def handle(self, *args, **options):
        if not Ingredient.objects.exists():
            with open('../DATA/ingredients.csv', 'r') as f:
                reader = csv.DictReader(f, fieldnames=['name', 'unit'])
                for row in reader:
                    Ingredient.objects.create(name=row.get('name'))

        if not Recipe.objects.exists():
            with open('../DATA/recipes.txt', 'r', newline='') as f:
                for line in f:
                    name = line.rstrip('\n')
                    Recipe.objects.create(name=name)
