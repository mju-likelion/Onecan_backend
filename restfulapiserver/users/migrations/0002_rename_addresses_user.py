# Generated by Django 3.2.5 on 2021-07-30 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addresses',
            new_name='User',
        ),
    ]
