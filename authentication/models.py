import os
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .validators import validate_phone_number


def user_photo_upload_path(instance, file):
    _, file_extension = os.path.splitext(file)
    file_path = 'users-photos/{}/profile_picture{}'.format(
        instance.phone_number,
        file_extension
    )
    return file_path


class CustomUserManager(UserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError(
                "user must have a phone number"
            )
        user = self.model(
            phone_number=phone_number,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            phone_number,
            password,
            **extra_fields
        )

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        return self._create_user(
            phone_number,
            password,
            **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class GenderChoices(models.TextChoices):
        MALE = "MALE", _("Male")
        FEMALE = "FEMALE", _("Female")
        OTHER = "OTHER", _('Other')

    phone_number = models.CharField(
        verbose_name=_('user phone number'),
        max_length=15,
        null=False,
        blank=False,
        unique=True,
        help_text=_(
            'Required. A valid phone number that doesnt excced 15 characters.'
        ),
        validators=[validate_phone_number],
        error_messages={
            'unique': _('A user with that phone number already exists.')
        }
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=200,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=200,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_('email address'),
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        verbose_name=_('user photo'),
        blank=True,
        null=True,
        upload_to=user_photo_upload_path
    )
    gender = models.CharField(
        verbose_name=_('gender'),
        max_length=10,
        null=True,
        blank=True,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE
    )
    date_of_birth = models.DateField(
        verbose_name=_('date of birth'),
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
            "By default the user is inactive"
        ),
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        )
    )
    date_joined = models.DateTimeField(
        verbose_name=_("date joined"),
        default=timezone.now
    )
    objects = CustomUserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('custom user')
        verbose_name_plural = _('custom users')
        ordering = ['-date_joined']

    def __str__(self):
        return self.phone_number

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name