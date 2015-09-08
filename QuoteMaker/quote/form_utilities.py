__author__ = 'harlanhaskins'
from django.core import validators
from django.core.exceptions import ValidationError

def none_if_invalid(item):
    """
    Takes advantage of python's 'falsiness' check by
    turning 'falsy' data (like [], "", and 0) into None.
    :param item: The item for which to check falsiness.
    :return: None if the item is falsy, otherwise the item.
    """
    return item if bool(item) else None


def email_is_valid(email):
    """
    Wrapper for Django's email validator that returns a boolean
    instead of requiring a try/catch block.
    :param email: The email to validate
    :return: Whether or not the email conforms to RFC 2822.
    """
    try:
        validators.validate_email(email)
        return True
    except ValidationError:
        return False
