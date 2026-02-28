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
        "delete": False,
        "archive": True,
    },
)
