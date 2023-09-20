from rest_framework.routers import DefaultRouter, Route

class CustomRouter(DefaultRouter):
    def get_routes(self, viewset):
        routes = super().get_routes(viewset)
        # Remove the detail route (retrieve view)
        return [route for route in routes if not isinstance(route, Route) or not route.name.endswith('-detail')]

from django.urls import path, include
from settings.api.viewset import SettingViewSet

app_name = 'setting_router'
router = CustomRouter()
router.register('', SettingViewSet, basename='settings')

urlpatterns = [
    path('', include(router.urls))
]
