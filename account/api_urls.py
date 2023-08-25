from django.urls import path, include


app_name = 'account'
urlpatterns = [
    path('account/', include('account.api.router')),
]
