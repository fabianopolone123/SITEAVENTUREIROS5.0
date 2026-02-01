"""Middleware helpers for the diagnostic system."""
import uuid

from django.utils.deprecation import MiddlewareMixin


class RequestIDMiddleware(MiddlewareMixin):
    """Garante que cada requisição carregue request_id no contexto."""

    def process_request(self, request):
        request.request_id = request.headers.get('X-Request-ID') or str(uuid.uuid4())
        request.trace_id = request.headers.get('X-Trace-ID')
        request.session_id = request.COOKIES.get('sessionid')

    def process_response(self, request, response):
        response.setdefault('X-Request-ID', getattr(request, 'request_id', 'unknown'))
        return response
