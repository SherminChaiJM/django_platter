from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from functools import wraps

def headoffice_required(view_func):
    def wrapper(request):
        if request.user.is_authenticated and request.user.is_headoffice:
            return view_func(request)
        else:
            raise PermissionDenied
    return wrapper

def districtoffice_required(view_func):
    def wrapper(request):
        if request.user.is_authenticated and request.user.is_districtoffice:
            return view_func(request)
        else:
            raise PermissionDenied
    return wrapper

def branchlocation_required(view_func):
    def wrapper(request):
        if request.user.is_authenticated and request.user.is_branchlocation:
            return view_func(request)
        else:
            raise PermissionDenied
    return wrapper


def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request):
            user = request.user
            if user.is_authenticated and any(getattr(user, role, False) for role in roles):
                return view_func(request)
            else:
                raise PermissionDenied
        return _wrapped_view
    return decorator