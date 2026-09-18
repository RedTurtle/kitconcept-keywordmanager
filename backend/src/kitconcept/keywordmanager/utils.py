from plone import api
from zExceptions.unauthorized import Unauthorized


def check_permission(func):
    """A function decorator that checks for a permission."""

    def wrapper(*args, **kwargs):
        if not api.user.has_permission("kitconcept.keywordmanager: Manage Keywords"):
            raise Unauthorized(
                "You are missing the required permissions to access this resource."
            )
        return func(*args, **kwargs)

    return wrapper
