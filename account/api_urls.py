from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from account.api.viewset import CustomTokenObtainPairViewSet

from account.api.router import router

app_name = 'account_urls'
urlpatterns = [
    path('account/', include('account.api.router')),
    
    path('account/token/',
         CustomTokenObtainPairViewSet.as_view(), name='token-login'),
    path('account/token/refresh/',
         TokenRefreshView.as_view(), name='token-refresh'),
    path('account/', include(router.urls)),
]
