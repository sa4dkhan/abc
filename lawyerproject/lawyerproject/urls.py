from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('website.urls')),
    path('', include('website.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('role', include('role.urls')),
    path('lawyer', include('lawyer.urls')),
    path('account/', include('account.urls')),
    path('client/', include('dashboard.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
