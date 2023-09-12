from rest_framework import routers
from django.urls import path
from settings.api.viewset import SettingViewSet


app_name = 'setting_router'
router = routers.DefaultRouter()

urlpatterns = [
    path('settings/',
         SettingViewSet.as_view(), name='settings'),
]
