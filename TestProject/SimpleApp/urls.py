from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_list_view, name='model_list'),  
    path('<int:pk>/update/', views.model_update_view, name='model_update'),  
    path('<int:pk>/delete/', views.model_delete_view, name='model_delete'),  
]