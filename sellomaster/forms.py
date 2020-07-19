from .models import mailus, Product
from django.forms import ModelForm, TextInput, EmailInput, Textarea

class mailusForm(ModelForm):
	class Meta:
		model = mailus
		fields = ['name', 'number', 'email', 'message']
		widgets = {
			'name': TextInput(attrs ={
				'class': 'form-control mt-4 ml-5 ',
				'placeholder': 'Введите ваше имя'
			}),
			'number': TextInput(attrs ={
				'class': 'form-control mt-4 ml-5 ',
				'placeholder': 'Введите ваш номер'
			}),
			'email': EmailInput(attrs ={
				'class': 'form-control mt-4 ml-5 ',
				'placeholder': 'Введите вашу почту'
			}),

			'message': Textarea(attrs ={
				'class': 'form-control mt-4 ml-5 ',
				'placeholder': 'Введите ваш текст'
			}),
		}

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ('title', 'description', 'number', 'country', 'image', 'price','currency', 'category')
