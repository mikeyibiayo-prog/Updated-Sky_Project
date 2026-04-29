"""
URL configuration for Sky_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from departments import views as dep_views
from organisation import views as org_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('messages.urls')),
    path('departments/', dep_views.departments_view, name='departments'),
    path('departments/platform-engineering/', dep_views.platform_engineering, name='platform_engineering'),
    path('departments/product-dev/', dep_views.product_dev, name='product_dev'),
    path('departments/mobile-app/', dep_views.mobile_app, name='mobile_app'),
    path('departments/human-resources/', dep_views.human_resources, name='human_resources'),
    path('departments/management/', dep_views.management, name='management'),
    path('departments/broadcasting/', dep_views.broadcasting, name='broadcasting'),
    path('organisation/', org_views.organisation_view, name='organisation'),
]