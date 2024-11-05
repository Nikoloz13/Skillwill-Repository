# myproject/testapp/urls.py
from django.urls import path
from .views import error_view

urlpatterns = [
    path('error/', error_view, name='error_view'),
]

