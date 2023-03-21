# Generated by Django 4.1.7 on 2023-03-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_tax_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_data',
            field=models.JSONField(blank=True, help_text="Data format: {'tax_type':{'tax_percentage':'tax_amount'}}", null=True),
        ),
    ]
