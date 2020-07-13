from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.blog,name='blogs'),
    path('create/',views.create_post,name='create'),
]
