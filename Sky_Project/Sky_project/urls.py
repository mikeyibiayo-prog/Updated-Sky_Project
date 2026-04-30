
from django.contrib import admin
from django.urls import path, include
from departments import views as dep_views
from organisation import views as org_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('teams/', include('teams.urls')),  # teams directory and profile pages
    path('', include('messages.urls')),
    path('departments/', dep_views.departments_view, name='departments'),
    path('departments/platform-engineering/', dep_views.platform_engineering, name='platform_engineering'),
    path('departments/product-dev/', dep_views.product_dev, name='product_dev'),
    path('departments/mobile-app/', dep_views.mobile_app, name='mobile_app'),
    path('departments/human-resources/', dep_views.human_resources, name='human_resources'),
    path('departments/management/', dep_views.management, name='management'),
    path('departments/broadcasting/', dep_views.broadcasting, name='broadcasting'),
    path('organisation/', org_views.organisation_view, name='organisation'),
    path('schedule/', include('schedule.urls')),
]