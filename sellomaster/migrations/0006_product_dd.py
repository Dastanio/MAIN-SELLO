# Generated by Django 3.0.8 on 2020-07-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellomaster', '0005_auto_20200713_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dd',
            field=models.CharField(default='', max_length=122),
        ),
    ]
