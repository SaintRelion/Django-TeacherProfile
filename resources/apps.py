from django.apps import AppConfig

from audit.utils import register


class ResourcesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "resources"

    def ready(self):
        # Serializers
        import resources.notification.serializers
        import resources.personal_information.serializers
        import resources.document_folder.serializers
        import resources.teacher_document.serializers
        import resources.teacher_performance.serializers
        import resources.user.serializers

        from resources.document_folder.models import DocumentFolder
        from resources.personal_information.models import PersonalInformation
        from resources.teacher_document.models import TeacherDocument

        register(
            DocumentFolder,
            PersonalInformation,
            TeacherDocument,
        )
