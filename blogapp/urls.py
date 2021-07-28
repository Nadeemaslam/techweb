from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('about/', views.about, name='about'),
    path(r'contact/', views.contact, name='contact'),
    path(r'blog/(?P<slug>[\w-]+)/$', views.detail, name='detail')
]