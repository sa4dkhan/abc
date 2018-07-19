from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.login_view, name='login'),
    path('validate_username/', views.validate_username, name='validate_username'),
]