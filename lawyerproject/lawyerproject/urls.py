from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from lawyerproject import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Built in Admin
    path('admin/', admin.site.urls),

    # Website
    path('', views.index, name='index'),

    # Admin Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Django User Authentication
    path('accounts/', include('django.contrib.auth.urls')),

    # Django Signup
    path('accounts/signup/', include('account.urls')),

    path('role', include('role.urls')),
    path('lawyer/', include('lawyer.urls')),
    path('account/', include('account.urls')),
    path('client/', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('change_password/', include('change_password.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
