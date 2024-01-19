from django.urls import path, include

app_name = "workspace"
urlpatterns = [
    path("workspaces/", include("workspace.api.router")),
]
