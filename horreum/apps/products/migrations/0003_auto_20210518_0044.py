# Generated by Django 3.1.7 on 2021-05-17 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210422_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_delted',
            new_name='is_deleted',
        ),
    ]
