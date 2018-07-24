from django.urls import path
from . import views
from .views import client_info, client_list, update_client, client_dashboard, store_client, update_form_action, delete_client, view_profile, update_profile

urlpatterns = [
    path('', views.index, name='dashboard_index'),
    path('dashboard/<int:id>', client_dashboard, name='client_dashboard'),
    path('client/', client_info, name='client_info'),
    path('client_list/', client_list, name='client_list'),
    path('update_client/<int:id>', update_client, name='update_client'),
    path('store_client', store_client, name='store_client'),
    path('update_form_action/<int:id>', update_form_action, name='update_form_action'),

    path('delete/<int:id>', delete_client, name='delete_client'),
    path('view_profile/<int:id>', view_profile, name='view_profile'),
    path('update_profile/<int:id>', update_profile, name='update_profile')
]
