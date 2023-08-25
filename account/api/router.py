from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from account.api.viewset import UserViewSet, ChangePasswordViewSet

app_name = 'accounts'

# Create the router for standard UserViewSet
router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    # Register standard UserViewSet URLs
    path('', include(router.urls)),

    # Custom ChangePasswordViewSet action URL
    path('change-password/', ChangePasswordViewSet.as_view({'put': 'change_password'}), name='change-password'),

    # JWT
    path('login/', TokenObtainPairView.as_view(), name='jwt-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
]
