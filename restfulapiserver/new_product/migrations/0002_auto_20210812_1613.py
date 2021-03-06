# Generated by Django 3.2.5 on 2021-08-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_product',
            old_name='body',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='new_product',
            name='title',
        ),
        migrations.AddField(
            model_name='new_product',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='new_product',
            name='price',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='new_product',
            name='product',
            field=models.CharField(default='', max_length=100),
        ),
    ]
