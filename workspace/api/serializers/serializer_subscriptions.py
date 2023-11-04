from rest_framework import serializers
import uuid
from workspace.models.model_workspace_invitation import WorkspaceInvitation
from workspace.models.model_workspace import Workspace
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from workspace.models import WorkspaceMember


class SubscriptionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages[
                    "required"
                ] = f"فیلد \
                `{field.label}` الزامی است."

    email = serializers.EmailField(required=True)

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages[
                    "required"
                ] = f"فیلد \
                `{field.label}` الزامی است."

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages[
                    "required"
                ] = f"فیلد \
                `{field.label}` الزامی است."

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

        workspace_member = WorkspaceMember.objects.create(
            workspace=workspace_invitation.workspace, user=user
        )

        workspace_invitation.expired = False
        workspace_invitation.save()

        return workspace_invitation
