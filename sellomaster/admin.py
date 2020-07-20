from django.contrib import admin

from .models import PostImage, Product, Comment, Category, Currency, Country, Mailus

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Currency)

class mailusAdmin(admin.ModelAdmin):
	list_display = ('name','message','number','email')
	list_display_links =('name', 'message')
admin.site.register(Mailus, mailusAdmin)

class PostImageAdmin(admin.StackedInline):
    model = PostImage


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'price','currency','country', 'number','date_publeshed', 'category')
	list_display_links = ('title', 'description')
	search_fields = ('title', 'description', )
	inlines = [PostImageAdmin]

	class Meta:
		model=Product
admin.site.register(Product, ProductAdmin)

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass