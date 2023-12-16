import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    if not re.match(r'^\+?1?\d{9,15}$', value):
        raise ValidationError(
            message=_('The phone number is not valid.'),
            code='invalid',
            params={
                'value': value
            }
        )


class PasswordIsEntirelyNumericValidator:
    """
    validate that the password is entirely numeric
    """

    def validate(self, password, user=None):
        if not password.isdigit():
            raise ValidationError(
                message=_('The password has to be entirely Numeric'),
                code='password_not_entirely_numeric',
                params={
                    'password': password
                }
            )

    def get_help_text(self):
        return _("Your password has to be entirely numeric.")