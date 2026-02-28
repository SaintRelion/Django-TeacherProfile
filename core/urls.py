from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("sr_libs.authentication.urls")),
    path("api/", include("sr_libs.dal.urls")),
]
