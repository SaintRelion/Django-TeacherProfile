from rest_framework import serializers, generics
from rest_framework.permissions import AllowAny
from .models import AuditLog


class AuditLogSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()

    class Meta:
        model = AuditLog
        fields = [
            "id",
            "timestamp",
            "user",
            "user_email",
            "action",
            "model_name",
            "object_id",
            "event",
            "data",
        ]

    def get_user_email(self, obj):
        return obj.user.email if obj.user_id else None


class AuditLogListView(generics.ListAPIView):
    serializer_class = AuditLogSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = (
            AuditLog.objects.select_related("user").defer("data").order_by("-timestamp")
        )
        for param in ("action", "model_name", "object_id", "event"):
            val = self.request.query_params.get(param)
            if val:
                qs = qs.filter(**{param: val})
        return qs
