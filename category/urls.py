from django.urls import path
from . import views

urlpatterns= [
    path('', views.index,name='categories'),
    path('<int:category_id', views.category, name='category'),

]