from sr_libs.dal.resource import register_resource
from ..teacher_document.models import TeacherDocument

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
        "create": [
            "id",
            "document_title",
            "issue_date",
            "expiry_date",
            "extension",
            "folder_id",
            "user_id",
            "file_base64",  # Keep file_base64 here for uploads
        ],
        "update": "__all__",
        "delete": False,
        "archive": True,
    },
)

register_resource(
    name="teacherdocumentfile",
    model=TeacherDocument,
    query_viewset=lambda: TeacherDocument.objects.all(),
    operations={
        "list": ["file_base64"],
        "retrieve": ["file_base64"],
        "create": False,
        "update": False,
        "delete": False,
        "archive": False,
    },
)
