from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .UserManager import UserManager
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    phonenumber = models.IntegerField(null=True)
    USER_TYPE_CHOICES = [("S", 'student'), ("T", 'teacher'), ]
    user_type = models.CharField(max_length=1,
                                 choices=USER_TYPE_CHOICES, default='S')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = "AUTH_USER_MODEL"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def is_student(self):
        return str(self.user_type) == "S"

    @property
    def is_teacher(self):
        return str(self.user_type) == "T"

    def __str__(self):
        return self.email
