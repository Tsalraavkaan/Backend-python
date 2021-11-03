from django.urls import path
from recipe.views import recipes, get_table

urlpatterns = [
    path('', recipes, name='recipes'),
    path('all/', get_table, name='get_table'),
]

