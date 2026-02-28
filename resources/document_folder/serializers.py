from sr_libs.dal.resource import register_resource
from ..document_folder.models import DocumentFolder

register_resource(
    name="documentfolder",
    model=DocumentFolder,
    operations={
        "list": True,
        "retrieve": "__all__",
        "create": "__all__",
        "update": "__all__",
        "delete": False,
        "archive": True,
    },
)
