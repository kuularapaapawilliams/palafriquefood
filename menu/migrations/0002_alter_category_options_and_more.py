# Generated by Django 4.1.4 on 2023-01-18 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Category_name',
            new_name='category_name',
        ),
    ]
