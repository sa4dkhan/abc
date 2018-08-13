from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='change_password'),
    # path('update', views.update, name='password_update'),



]
