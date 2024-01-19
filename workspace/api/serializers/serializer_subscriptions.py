import uuid
from rest_framework import serializers
from workspace.models.model_workspace_invitation import WorkspaceInvitation
from django.shortcuts import get_object_or_404
from workspace.models import WorkspaceMember, Workspace


class WorkSpaceForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context["request"].user
        return Workspace.objects.filter(workspace_members__user=user)


class SubscriptionSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    workspace = WorkSpaceForeignKey()

    class Meta:
        model = WorkspaceInvitation
        fields = ["workspace", "email"]

    def create(self, validated_data):
        token = uuid.uuid4().hex
        workspace_invitation = WorkspaceInvitation.objects.create(
            token=token, workspace=validated_data["workspace"]
        )
        return workspace_invitation


class SubscriptionCopySerializer(serializers.ModelSerializer):
    workspace = WorkSpaceForeignKey()

    class Meta:
        model = WorkspaceInvitation
        fields = ["workspace"]

    def create(self, validated_data):
        token = uuid.uuid4().hex
        workspace_invitation = WorkspaceInvitation.objects.create(
            token=token, workspace=validated_data["workspace"]
        )
        return workspace_invitation


class SubscriptionInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceInvitation
        fields = ["token"]

    def create(self, validated_data):
        user = self.context["request"].user
        workspace_invitation = get_object_or_404(
            WorkspaceInvitation, token=validated_data["token"]
        )

        if workspace_invitation.expired:
            return serializers.ValidationError(
                {"verification_code": ("این دعوت نامه منقضی شده.")}
            )

        WorkspaceMember.objects.get_or_create(
            workspace=workspace_invitation.workspace, user=user
        )
        workspace_invitation.expired = False
        workspace_invitation.save()
        return workspace_invitation
