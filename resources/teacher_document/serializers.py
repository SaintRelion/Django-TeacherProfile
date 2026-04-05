from sr_libs.dal.resource import register_resource
from ..teacher_document.models import TeacherDocument
from rest_framework import serializers

register_resource(
    name="teacherdocument",
    model=TeacherDocument,
    query_viewset=lambda: TeacherDocument.objects.all().defer("file_base64"),
    operations={
        "list": [
            "id",
            "is_archived",
            "document_title",
            "issue_date",
            "expiry_date",
            "extension",
            "file_size_in_mb",
            "created_at",
            "updated_at",
            "folder_id",
            "user_id",
        ],
        "retrieve": [
            "id",
            "user_id",
            "is_archived",
            "document_title",
            "issue_date",
            "expiry_date",
            "extension",
            "file_size_in_mb",
            "created_at",
            "updated_at",
            "folder_id",
        ],
        "create": "__all__",
        "update": "__all__",
        "delete": False,
        "archive": True,
    },
)


class TeacherDocumentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherDocument
        fields = ["id", "file_base64"]
