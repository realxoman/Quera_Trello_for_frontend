from django.urls import path
from rest_framework import routers

from account.api.viewset import (
    UserRegisterViewSet,
    ChangePasswordViewSet,
    ResetPasswordViewSet,
    ResetPasswordTokenViewSet,
    SetPasswordViewSet
)

router = routers.DefaultRouter()


urlpatterns = [
    # Registration
    path('register/',
         UserRegisterViewSet.as_view({'post': 'create'}), name='register'),

    # Change/Reset password
    path('change-password/', ChangePasswordViewSet.as_view(
        {'put': 'change_password'}), name='change-password'),
    path("reset-password/", ResetPasswordViewSet.as_view(),
         name="reset-password-request"),
    path("reset-password/validate-token/",
         ResetPasswordTokenViewSet.as_view(), name="reset-password-validate"),
    path("reset-password/set-password/",
         SetPasswordViewSet.as_view(), name="reset-password-confirm"),
]
