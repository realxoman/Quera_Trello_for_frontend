from rest_framework import permissions

class ProjectMemberPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check the user's permission based on the role field in ProjectMember
        user = request.user
        
        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True  # Superusers have full access

        if view.action in 'create':
            return True

        project_member = user.projectmember_set.filter(project=view.kwargs.get('project_id')).first()

        workspace_member = user.workspacemember_set.filter(workspace=view.kwargs.get('workspace_id')).first()

        if workspace_member and workspace_member.is_super_access:
            return True

        if project_member and project_member.role >= view.required_permission:
            return True

        return False
