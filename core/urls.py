from django.contrib import admin
from django.urls import path, include

from accounts.views import ResetPasswordView, SendResetLinkView
from resources.teacher_document.views import TeacherDocumentFileView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("sr_libs.authentication.urls")),
    path("api/", include("sr_libs.dal.urls")),
    path(
        "api/teacher-document-file/<int:pk>/",
        TeacherDocumentFileView.as_view(),
        name="teacher-document-file",
    ),
    path(
        "api/accounts/send-reset-link/",
        SendResetLinkView.as_view(),
        name="send-reset-link",
    ),
    path(
        "api/accounts/reset-password/",
        ResetPasswordView.as_view(),
        name="reset-password",
    ),
]
