# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home_view, name='home'),  # Homepage URL
    path('name', views.name_view, name='name'),
    path('hobby', views.hobby_view, name='hobby'),
    path('dream', views.dream_view, name='dream'),
]
