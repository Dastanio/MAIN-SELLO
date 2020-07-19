from django.db import models
from datetime import date
from django.utils import timezone

class mailus(models.Model):
	name = models.CharField('Имя',max_length=50)
	email = models.CharField('email',max_length=100)
	number =  models.CharField('Номер',max_length=250)
	message = models.TextField('Сообщения')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Сообщении"


class Country(models.Model):
	country = models.CharField('country', max_length = 64, default='')

	def __str__(self):
		return self.country
	class Meta:
		verbose_name_plural = "Страны"

class Currency(models.Model):
	currency = models.CharField('currency', max_length = 64, default='')

	def __str__(self):
		return self.currency
	class Meta:
		verbose_name_plural = "Валюты"

class Category(models.Model):
	category = models.CharField('title', max_length = 64,db_index =True, default='')

	def __str__(self):
		return self.category
	class Meta:
		verbose_name_plural = "Категорий"
		ordering = ['category']

class Product(models.Model):
	category = models.ForeignKey(Category,null =True, on_delete =models.PROTECT, default='')
	title = models.CharField('Заголовок',max_length=30)
	description = models.TextField('Описания')
	number = models.CharField('Номер телефона',max_length=50)
	country = models.ForeignKey(Country,on_delete =models.CASCADE, default ='')
	image = models.ImageField('Изображения',blank=True)
	price = models.IntegerField('Цена',default=0)
	currency = models.ForeignKey(Currency,on_delete =models.CASCADE, default ='')
	draft = models.BooleanField('Черновек',default=False)
	date_publeshed = models.DateField(auto_now_add=True)


	def was_publish_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural = "Товары"

class PostImage(models.Model):
	post = models.ForeignKey(Product, default=None,blank=True, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.post.title

	class Meta:
		verbose_name_plural = "Пост изображении"


class Comment(models.Model):
	author_name = models.CharField('Имя автора', max_length = 64)
	comment_text = models.TextField('Текст комментария')
	date_pub = models.DateTimeField(auto_now_add=True)
	product = models.ForeignKey(Product, on_delete =models.CASCADE)

	def was_publish_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	def __str__(self):
		return self.author_name
	class Meta:
		verbose_name_plural = "комментарии"

