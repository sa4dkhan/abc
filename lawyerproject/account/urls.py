from django.urls import path
from account import views


app_name = "account"
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('password/', views.change_password, name='change_password'),
]