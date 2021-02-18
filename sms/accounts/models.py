from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError(_("User should have an email"))
        if not password:
            raise ValueError(_("User should have an password"))
        if not user_name:
            raise ValueError(_("User should have an user_name"))
        if not first_name:
            raise ValueError(_("User should have an first_name"))

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name, first_name=first_name,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("SuperUser must be assigned to is_staff=True.")
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                "SuperUser must be assigned to is_superuser=True.")

        return self.create_user(email=email, password=password, user_name=user_name, first_name=first_name, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    TYPE_OF_USER = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]
    email = models.EmailField(_("Email Address"), unique=True)
    user_name = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    type_of_user = models.CharField(
        max_length=10, choices=TYPE_OF_USER, default=STUDENT)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_fullname(self):
        return self.first_name+" "+self.last_name

    def get_shortname(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def is_student(self):
        return self.type_of_user == User.STUDENT

    def is_teacher(self):
        return self.type_of_user == User.TEACHER
