from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from account.api.viewset import (
    UserViewSet,
    ChangePasswordViewSet,
    ResetPasswordViewSet,
    ResetPasswordTokenViewSet,
    SetPasswordViewSet
)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    # Registration
    path('', include(router.urls)),

    # Change/Reset password
    path('change-password/', ChangePasswordViewSet.as_view(
        {'put': 'change_password'}), name='change-password'),
    path("reset-password/", ResetPasswordViewSet.as_view(),
         name="reset-password-request"),
    path("reset-password/validate-token/",
         ResetPasswordTokenViewSet.as_view(), name="reset-password-validate"),
    path("reset-password/set-password/",
         SetPasswordViewSet.as_view(), name="reset-password-confirm"),

    # JWT
    path('login/', TokenObtainPairView.as_view(), name='jwt-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
]
