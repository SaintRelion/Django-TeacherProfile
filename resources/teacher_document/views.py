from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import TeacherDocument
from .serializers import TeacherDocumentFileSerializer
from rest_framework.permissions import AllowAny


class TeacherDocumentFileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        document = get_object_or_404(TeacherDocument, pk=pk)
        serializer = TeacherDocumentFileSerializer(document)
        return Response(serializer.data)
