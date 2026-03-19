from sr_libs.dal.resource import register_resource
from .models import User

register_resource(
    name="user",
    model=User,
    operations={
        "list": ["id", "first_name", "last_name", "email", "username", "date_joined"],
        "retrieve": [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "date_joined",
        ],
        "update": "__all__",
        "delete": True,
        "archive": True,
    },
)
