from django.http import HttpRequest

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class HomepageView(APIView):
    """Define simple home api view."""

    permission_classes = (permissions.AllowAny,)

    def get(self, request: HttpRequest) -> Response:
        """Return simple http response."""
        return Response('PythonGroup API')
