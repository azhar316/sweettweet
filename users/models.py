from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, UnicodeUsernameValidator)


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_staff_user(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('staff/superuser must have is_staff=True')

        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')

        return self.create_staff_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': "A user with that username already exists",
        },
    )
    email = models.EmailField(unique=True, error_messages={
            'unique': "A user with that username already exists",
        },)
    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into admin site"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Designates whether the user is active. Unselect this instead of deleting accounts"
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def get_email(self):
        return self.email

    @property
    def is_admin(self):
        return self.is_superuser

    # Enable staff users all the permissions to perform actions
    # in admin site
    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_perms(self, perm_list, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
