# Generated by Django 4.1.4 on 2023-01-13 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='logitude',
            new_name='longitude',
        ),
    ]
