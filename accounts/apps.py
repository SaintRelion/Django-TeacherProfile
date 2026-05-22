from django.apps import AppConfig
from audit.utils import register


class AccountsConfig(AppConfig):
    name = "accounts"

    def ready(self):
        from .serializer import UserRegisterSerializer, MeSerializer
        from sr_libs.authentication.resource import define_register, define_me

        from accounts.models import User

        define_register(serializer=UserRegisterSerializer)
        define_me(serializer=MeSerializer)

        register(User)
