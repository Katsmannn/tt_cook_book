import csv
from django.conf import settings

from django.core.management.base import BaseCommand, CommandError

from recipes.models import Product, Recipe


class Command(BaseCommand):
    help = "Create data in db"

    def handle(self, *args, **options):
        if not Product.objects.exists():
            # print(settings.BASE_DIR.joinpath('DATA').joinpath('ingredients.csv'))
            with open(
                settings.BASE_DIR.parent.joinpath('DATA').joinpath('ingredients.csv'), 'r'
            ) as f:
                reader = csv.DictReader(f, fieldnames=['name', 'unit'])
                for row in reader:
                    Product.objects.create(name=row.get('name'))

        if not Recipe.objects.exists():
            with open(
                settings.BASE_DIR.parent.joinpath('DATA').joinpath('recipes.txt'), 'r'
            ) as f:
                for line in f:
                    name = line.rstrip('\n')
                    Recipe.objects.create(name=name)
