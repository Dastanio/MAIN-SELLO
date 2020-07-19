from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from .models import PostImage, Product, Category
from .forms import mailusForm, ProductForm
from django.urls import reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class ProductCreateView(CreateView):
	template_name = 'create.html'
	form_class = ProductForm
	success_url = reverse_lazy('add')


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rubrics'] = Category.objects.all()
		return context


def blog_view(request):
    posts = Product.objects.order_by('-date_publeshed')
    rubrics = Category.objects.all()
    return render(request, 'blog.html', {'posts':posts, 'rubrics':rubrics})

def detail_view(request, id):
	post = get_object_or_404(Product, id=id)

	latest_comments_list = post.comment_set.order_by('-id')[:10]

	photos = PostImage.objects.filter(post=post)
	context = {
		'post':post,
		'photos':photos,
		'latest_comments_list':latest_comments_list
	}
	return render(request, 'detail.html', context)
def leave_comment(request, id):
	try:
		post = Product.objects.get(id=id)
	except:
		raise Http404('Обьявлений не найдено')

	post.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('detail', args = (post.id,)) )

def about(request):
	if request.method == 'POST':
		form =mailusForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ('Вы успешно отправили сообщения!'))
			return redirect('about')



	form = mailusForm()
	context = {
		'form':form
	}
	return render(request, 'about.html', context)


def by_rubric(request, rubric_id):
	bbs = Product.objects.filter(category=rubric_id)
	rubrics = Category.objects.all()
	current_rubric = Category.objects.get(pk=rubric_id)
	context = {
		'rubrics':rubrics,
		'bbs':bbs,
		'current_rubric':current_rubric,
	}
	return render(request, 'category.html', context)