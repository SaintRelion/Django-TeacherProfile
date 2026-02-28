from sr_libs.dal.resource import register_resource
from ..notification.models import Notification

register_resource(
    name="notification",
    model=Notification,
    operations={
        "list": True,
        "retrieve": "__all__",
        "create": "__all__",
        "update": "__all__",
        "delete": False,
        "archive": True,
    },
)
