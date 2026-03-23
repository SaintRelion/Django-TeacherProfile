from sr_libs.dal.resource import register_resource
from ..personal_information.models import PersonalInformation

register_resource(
    name="personalinformation",
    model=PersonalInformation,
    operations={
        "list": True,
        "retrieve": "__all__",
        "create": "__all__",
        "update": "__all__",
        "delete": True,
        "archive": True,
    },
)

from rest_framework.permissions import IsAdminUser, IsAuthenticated

register_resource(
    name="inspect_personalinformation",  # new API endpoint
    model=PersonalInformation,
    operations={
        "list": "__all__",
        "retrieve": "__all__",
        "create": "__all__",
        "update": True,
    },
    permissions={
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
    },
)
