from rest_framework_nested import routers
from django.urls import path, include

from workspace.api.viewset import (
    WorkspaceViewSet, WorkspaceMemberViewSet, ProjectsViewSet,
    ProjectMemberViewSet, BoardViewSet, TaskViewSet,
    TaskCommentViewSet, TaskAssigneeViewSet, TaskLogViewSet,
    SubscriptionViewSet
)


app_name = 'workspace_router'
router = routers.DefaultRouter()
router.register('', WorkspaceViewSet, basename='workspace')

# Workspaces endpoints
workspaces_routers = routers.NestedDefaultRouter(
    router, '', lookup='workspace')
workspaces_routers.register(
    'members', WorkspaceMemberViewSet, basename='workspace-members')
workspaces_routers.register('projects', ProjectsViewSet, basename='projects')

# Projects endpoints
projects_routers = routers.NestedDefaultRouter(
    workspaces_routers, 'projects', lookup='project')
projects_routers.register(
    'members', ProjectMemberViewSet, basename='project-members')
projects_routers.register('boards', BoardViewSet, basename='boards')

# Boards endpoints
boards_routers = routers.NestedDefaultRouter(
    projects_routers, 'boards', lookup='board')
boards_routers.register('tasks', TaskViewSet, basename='board-tasks')

# Tasks endpoints
tasks_routers = routers.NestedDefaultRouter(
    boards_routers, 'tasks', lookup='task')
tasks_routers.register(
    'assignee', TaskAssigneeViewSet, basename='task-assignee')
tasks_routers.register(
    'comments', TaskCommentViewSet, basename='task-comments')
tasks_routers.register(
    'logs', TaskLogViewSet, basename='task-logs')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(workspaces_routers.urls)),
    path(r'', include(projects_routers.urls)),
    path(r'', include(boards_routers.urls)),
    path(r'', include(tasks_routers.urls)),
    path('subescriptions', SubscriptionViewSet.as_view(), name="subscription")
]
