from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "accounts"

    def ready(self):
        from .serializer import UserRegisterSerializer, MeSerializer
        from sr_libs.authentication.resource import define_register, define_me

        define_register(serializer=UserRegisterSerializer)
        define_me(serializer=MeSerializer)
