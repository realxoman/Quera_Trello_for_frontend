from django.urls import path, include


app_name = 'account_urls'
urlpatterns = [
    path('account/', include('account.api.router')),
]
