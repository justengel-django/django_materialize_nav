"""django_materialize_nav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('demo.urls')),

    # path('login/', auth_views.login, name='login'),
    # path('logout/', auth_views.logout, {"next_page": "/login/"}, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]


# Development
from django.conf import settings
if settings.DEBUG:
    # Serve static files
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Debug toolbar urls
    try:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        pass
