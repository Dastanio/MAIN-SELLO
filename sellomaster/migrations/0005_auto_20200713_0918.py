# Generated by Django 3.0.8 on 2020-07-13 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellomaster', '0004_auto_20200713_0844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='prodcut',
            new_name='product',
        ),
    ]