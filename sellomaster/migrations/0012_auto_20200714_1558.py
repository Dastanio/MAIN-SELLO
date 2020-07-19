# Generated by Django 3.0.8 on 2020-07-14 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellomaster', '0011_auto_20200714_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Категорий'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(db_index=True, default='', max_length=64, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='sellomaster.Category'),
        ),
    ]
