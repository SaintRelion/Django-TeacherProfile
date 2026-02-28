from sr_libs.dal.resource import register_resource
from .models import User

register_resource(
    name="user",
    model=User,
    operations={
        "list": True,
        "retrieve": "__all__",
        "update": "__all__",
        "delete": False,
        "archive": True,
    },
)
