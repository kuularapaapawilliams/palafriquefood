# Generated by Django 4.1.4 on 2023-01-18 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditem',
            old_name='Category',
            new_name='category',
        ),
    ]
