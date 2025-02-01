from django.urls import path
from .views import *

urlpatterns = [
    path('news/', index),
    path('get', get_name),
    path('del', delete_name),
]