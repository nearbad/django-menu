from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('<str:menu_name>/', MenuView.as_view(), name='menu'),
    path('', index, name='index'),

]
