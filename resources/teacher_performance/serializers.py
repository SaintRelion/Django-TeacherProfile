from sr_libs.dal.resource import register_resource
from ..teacher_performance.models import TeacherPerformance

register_resource(
    name="teacherperformance",
    model=TeacherPerformance,
    operations={
        "list": True,
        "retrieve": "__all__",
        "create": "__all__",
        "update": "__all__",
        "delete": False,
        "archive": True,
    },
)
