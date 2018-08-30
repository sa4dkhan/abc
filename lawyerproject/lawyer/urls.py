from django.urls import path, include
from . import views
from .views import create_lawyer, store_lawyer, lawyer_list, view_lawyer_update, delete_lawyer, update_form_action_lawyer, search
from rest_framework import routers

router = routers.DefaultRouter()
router.register('lawyer', views.LawyerView)

urlpatterns = [
    path('/api/', include(router.urls)),
    path('', views.index, name='dashboard_index'),
    path('create_lawyer/', create_lawyer, name='create_lawyer'),
    path('store_lawyer/', store_lawyer, name='store_lawyer'),
    path('lawyer_list/', lawyer_list, name='lawyer_list'),
    path('view_lawyer_update/<int:id>/', view_lawyer_update, name='view_lawyer_update'),
    path('delete/<int:id>/', delete_lawyer, name='delete_lawyer'),
    path('update_form_action_lawyer/<int:id>/', update_form_action_lawyer, name='update_form_action_lawyer'),
    path('search/', search, name='search'),
]
