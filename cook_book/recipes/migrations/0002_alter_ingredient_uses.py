# Generated by Django 4.2.9 on 2024-01-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='uses',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
