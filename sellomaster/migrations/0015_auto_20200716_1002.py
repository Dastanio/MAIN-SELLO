# Generated by Django 3.0.8 on 2020-07-16 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellomaster', '0014_auto_20200716_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, default='', max_length=64, verbose_name='title')),
            ],
            options={
                'verbose_name_plural': 'Категорий',
                'ordering': ['category'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='sellomaster.Category'),
        ),
    ]
