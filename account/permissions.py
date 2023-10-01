from rest_framework import permissions

class ProjectMemberPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check the user's permission based on the role field in ProjectMember
        user = request.user
        
        if not user.is_authenticated():
            return False

        if user.is_superuser:
            return True  # Superusers have full access

        if view.action in 'create':
            return True

        project_member = user.project_members_set.filter(project=view.kwargs.get('project_pk')).first()

        workspace_member = user.workspace_members_set.filter(project=view.kwargs.get('project_pk')).first()

        if workspace_member.is_super_access:
            return True

        user_role = project_member.role

        if user_role >= view.required_permission:
            return True

        return False
