# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.utils.deconstruct import deconstructible

import uuid as uuid_lib


@deconstructible
class NameValidator(validators.RegexValidator):
    regex = r'^[\w-]+$'
    message = 'Enter a valid username. This value may contain only letters, numbers, and -/_ characters.'
    flags = 0


class User(AbstractBaseUser):
    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)
    name_validator = NameValidator()
    name = models.CharField(
            max_length=150,
            unique=True,
            validators=[name_validator],
            error_messages={
                'unique': "A user with that username already exists.",
            },
    )

    first_name = models.CharField(max_length=32, blank=True, help_text="名前")
    last_name = models.CharField(max_length=32, blank=True, help_text="苗字")

    email_validator = validators.EmailValidator()
    email = models.EmailField(
            unique=True,
            validators=[email_validator],
            error_messages={
                'unique': "A email already exists.",
            },
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "name"

    class Meta:
        db_table = 'user'

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # importを特別に処理直前に読んでいる
        # from accounts import services
        # services.after_save_user(self)
