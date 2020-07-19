from django.urls import path

from . import views
from .views import ProductCreateView
urlpatterns = [
    path('', views.blog_view, name = 'blog'),
    path('detail/<int:id>/', views.detail_view, name = 'detail'),
    path('detail/<int:id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('add/', ProductCreateView.as_view(), name = 'add'),
	path('<int:rubric_id>/', views.by_rubric, name = 'by_rubric'),
	path('about/', views.about, name ='about'),
]