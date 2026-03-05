from sr_libs.dal.resource import register_resource
from ..teacher_document.models import TeacherDocument

register_resource(
    name="teacherdocument",
    model=TeacherDocument,
    query_viewset=lambda: TeacherDocument.objects.all(),
    operations={
        "list": True,
        "retrieve": "__all__",
        "create": "__all__",
        "update": "__all__",
        "delete": False,
        "archive": True,
    },
)
