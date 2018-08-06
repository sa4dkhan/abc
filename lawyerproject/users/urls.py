from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('create', views.create, name='user_create'),
    path('user_store', views.store, name='user_store'),
    path('edit/<int:id>', views.edit, name='user_edit'),
    path('update/<int:id>', views.update, name='user_update'),
    path('delete/<int:id>', views.delete, name='user_delete'),

]
