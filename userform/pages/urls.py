from django.contrib import admin
from django.urls import path
from pages.views import form, user_info, get_table
from django.views.generic import TemplateView

urlpatterns = [
    path('', form, name='form'),
    path('user/', user_info, name='user_info'),
    path('data/', get_table, name='get_table'),
]

