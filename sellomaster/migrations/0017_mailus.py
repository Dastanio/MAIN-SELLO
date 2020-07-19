# Generated by Django 3.0.8 on 2020-07-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellomaster', '0016_auto_20200716_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='mailus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('number', models.CharField(max_length=250, verbose_name='Номер')),
                ('message', models.TextField(verbose_name='Сообщения')),
            ],
            options={
                'verbose_name_plural': 'Сообщении',
            },
        ),
    ]
