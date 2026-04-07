from rest_framework import serializers, exceptions

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    roles = serializers.ListField(child=serializers.CharField(), write_only=True)
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id"]

    def validate(self, attrs: dict) -> dict:
        username: str = attrs.get("username", "")
        email: str = attrs.get("email", "")
        target_username: str = username if username else email

        if User.objects.filter(username=target_username).exists():
            # We use PermissionDenied or a custom Exception to bypass DRF's
            # automatic list-wrapping of ValidationErrors.
            # This ensures the output is {"detail": "message"} NOT {"detail": ["message"]}
            exc = exceptions.APIException("A user with this username already exists.")
            exc.status_code = 400
            raise exc

        return attrs

    def create(self, validated_data: dict):
        roles: list[str] = validated_data.pop("roles", [])
        password: str = validated_data.pop("password")

        # Username logic (already validated in validate() above)
        if not validated_data.get("username"):
            validated_data["username"] = validated_data.get("email")

        try:
            # create_user handles password hashing and internal user logic
            user = User.objects.create_user(password=password, **validated_data)

            for role_name in roles:
                group, _ = Group.objects.get_or_create(name=role_name)
                user.groups.add(group)

            return user

        except Exception as e:
            # Force the exception message to a string to satisfy 'handleFetch'
            exc = exceptions.APIException(str(e))
            exc.status_code = 400
            raise exc


class MeSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "roles", "pds"]

    def get_roles(self, obj):
        return list(obj.groups.values_list("name", flat=True))
