import logging

logger = logging.getLogger("django.request")


class ExceptionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception:
            logger.exception(
                "Unhandled exception on %s %s",
                request.method,
                request.path,
            )
            raise