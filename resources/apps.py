from django.apps import AppConfig


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
