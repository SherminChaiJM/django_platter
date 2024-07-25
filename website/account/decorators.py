from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from functools import wraps

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
