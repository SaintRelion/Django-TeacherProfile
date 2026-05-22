import threading

_local = threading.local()


def set_current_user(user):
    _local.user = user


def current_user():
    request = getattr(_local, "request", None)
    if not request:
        return None
    user = getattr(request, "user", None)
    if user and user.is_authenticated:
        return user
    return None


class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _local.request = request
        response = self.get_response(request)
        return response
