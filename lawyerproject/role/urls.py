from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='role_index'),
    path('create', views.create, name='role_create'),
    path('delete/<int:id>', views.delete, name='role_delete'),
    path('update/<int:id>', views.update, name='role_update'),
]