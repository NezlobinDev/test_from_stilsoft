from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    """Custom pagination class with extra attributes."""

    page_size_query_param = 'page_size'

    def get_paginated_response(self, serializer_data):
        """Returns paginated response."""
        return Response(
            OrderedDict([
                # base
                ('count', self.page.paginator.count),
                ('page_size', self.get_page_size(self.request)),

                # extra
                (
                    'previous',
                    self.page.previous_page_number()
                    if self.page.has_previous()
                    else None,
                ),
                ('current', self.page.number),
                (
                    'next',
                    self.page.next_page_number()
                    if self.page.has_next()
                    else None,
                ),

                # data
                ('results', serializer_data),
            ]),
        )
