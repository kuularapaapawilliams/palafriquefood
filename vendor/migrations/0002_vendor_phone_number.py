# Generated by Django 4.1.4 on 2023-01-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]