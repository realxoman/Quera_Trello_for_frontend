from rest_framework import routers
from django.urls import path, include
from settings.api.viewset import SettingViewSet


app_name = 'setting_router'
router = routers.DefaultRouter()
router.register('settings', SettingViewSet, basename='settings')

urlpatterns = [
    path('', include(router.urls))
]