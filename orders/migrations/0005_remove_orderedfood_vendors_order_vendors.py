# Generated by Django 4.1.4 on 2023-03-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_alter_openinghour_options_and_more'),
        ('orders', '0004_order_total_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedfood',
            name='vendors',
        ),
        migrations.AddField(
            model_name='order',
            name='vendors',
            field=models.ManyToManyField(blank=True, to='vendor.vendor'),
        ),
    ]
