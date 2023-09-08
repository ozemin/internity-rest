from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from uuid import uuid4
from django.utils import timezone


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()

        return user


roles = (
    ('admin', 'Admin'),
    ('recruiter', 'Recruiter'),
    ('intern', 'Intern'),
)


class User(AbstractBaseUser, PermissionsMixin):
    userId = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=roles, default='intern')
    is_staff = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['createdAt']
