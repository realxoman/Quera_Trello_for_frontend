from django.urls import path, include


app_name = 'setting'
urlpatterns = [
    path('settings/', include('settings.api.router')),
]
