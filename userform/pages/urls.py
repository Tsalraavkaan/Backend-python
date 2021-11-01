from django.contrib import admin
from django.urls import path
from pages.views import form, info
from django.views.generic import TemplateView

urlpatterns = [
    path('', form, name='form'),
    path('info/', info, name='info'),
]

