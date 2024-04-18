"""
URL configuration for margdarshak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from awsapi.views import (
    ZoneListCreate, ZoneRetrieveUpdateDestroy,
    AreaListCreate, AreaRetrieveUpdateDestroy,
    ClusterListCreate, ClusterRetrieveUpdateDestroy,
    WLSUListCreate, WLSURetrieveUpdateDestroy,
    CedativeListCreate, CedativeRetrieveUpdateDestroy,
    get_water_level_data
)

urlpatterns = [
    path('zones/', ZoneListCreate.as_view(), name='zone-list'),
    path('zones/<pk>/', ZoneRetrieveUpdateDestroy.as_view(), name='zone-detail'),
    path('areas/', AreaListCreate.as_view(), name='area-list'),
    path('areas/<pk>/', AreaRetrieveUpdateDestroy.as_view(), name='area-detail'),
    path('clusters/', ClusterListCreate.as_view(), name='cluster-list'),
    path('clusters/<pk>/', ClusterRetrieveUpdateDestroy.as_view(), name='cluster-detail'),
    path('wlsus/', WLSUListCreate.as_view(), name='wlsu-list'),
    path('wlsus/<pk>/', WLSURetrieveUpdateDestroy.as_view(), name='wlsu-detail'),
    path('cedatives/', CedativeListCreate.as_view(), name='cedative-list'),
    path('cedatives/<pk>/', CedativeRetrieveUpdateDestroy.as_view(), name='cedative-detail'),
    path("admin/", admin.site.urls),
    path("get_water_level_data/",get_water_level_data,name="get_water_level_data")
]