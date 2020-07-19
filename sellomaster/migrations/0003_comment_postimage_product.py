# Generated by Django 3.0.8 on 2020-07-13 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellomaster', '0002_auto_20200713_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описания')),
                ('contact', models.CharField(max_length=100, verbose_name='Контакты')),
                ('number', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('country', models.CharField(max_length=60, verbose_name='Страна')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Изображения')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновек')),
                ('date_publeshed', models.DateTimeField(verbose_name='Дата публикации')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sellomaster.Category')),
            ],
            options={
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sellomaster.Product')),
            ],
            options={
                'verbose_name_plural': 'Пост изображении',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=64, verbose_name='Имя автора')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('date_pub', models.DateTimeField(verbose_name='Дата публикации')),
                ('prodcut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellomaster.Product')),
            ],
            options={
                'verbose_name_plural': 'комментарии',
            },
        ),
    ]
