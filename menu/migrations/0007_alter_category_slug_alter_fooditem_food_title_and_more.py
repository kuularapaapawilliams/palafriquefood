# Generated by Django 4.1.7 on 2023-03-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_category_slug_alter_fooditem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='food_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]