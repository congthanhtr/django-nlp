from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vietnamese', views.vietnamese, name='vietnamese'),
    path('english', views.english, name='english'),
]