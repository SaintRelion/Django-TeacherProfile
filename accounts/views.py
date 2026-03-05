from datetime import timedelta

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from sr_libs.delivery_channels.services.email import send_email

User = get_user_model()


class SendResetLinkView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response(
                {"detail": "Email is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Optional: don't reveal if email exists
            return Response(
                {"detail": "If this email exists, a reset link has been sent."}
            )

        # Create short-lived JWT
        token = AccessToken.for_user(user)
        token.set_exp(lifetime=timedelta(seconds=240))  # 4 minutes

        # Build reset link for frontend
        frontend_base = "https://teacherprofiling-kc.online/"
        reset_url = f"{frontend_base}reset-password/?token={str(token)}"

        send_email(
            subject="Password Reset",
            message=f"Hi {user.username}, click here to reset your password: {reset_url}",
            recipient_list=[user.email],
        )

        return Response({"detail": "If this email exists, a reset link has been sent."})


class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token_str = request.data.get("token")
        new_password = request.data.get("password")

        if not token_str or not new_password:
            return Response(
                {"detail": "Token and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = AccessToken(token_str)
            user_id = token["user_id"]
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password reset successfully."})
        except Exception:
            return Response(
                {"detail": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )
