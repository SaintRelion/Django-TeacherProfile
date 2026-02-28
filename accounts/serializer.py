from rest_framework import serializers

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

    def create(self, validated_data):
        roles = validated_data.pop("roles", [])
        password = validated_data.pop("password")

        # Set username = email if not provided
        if "username" not in validated_data or not validated_data["username"]:
            validated_data["username"] = validated_data.get("email", None)
            if validated_data["username"] is None:
                raise serializers.ValidationError("Email is required for username.")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        for role_name in roles:
            group, _ = Group.objects.get_or_create(name=role_name)
            user.groups.add(group)

        return user


class MeSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = fields = [
            "id",
            "username",
            "email",
            "roles",
        ]

    def get_roles(self, obj):
        return list(obj.groups.values_list("name", flat=True))
