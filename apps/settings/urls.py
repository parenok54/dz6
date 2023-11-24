from django.urls import path
from apps.settings import views
urlpatterns = [
    path('', views.index, name="index"),
    path('blog', views.blog, name="blog"),
    path('single_post', views.single_post, name="single_post")
]