# Generated by Django 3.2.6 on 2021-08-10 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_addresses_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='password1',
        ),
    ]
