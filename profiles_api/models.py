from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):                          # Inheritance from AbstractBaseUser and PermissionsMixin allows us to base our abstract user model
    """Database model for users in the system"""                                # on default Django user model.
    email = models.EmailField(max_lenght = 255, unique = True)                  # With every EmailField we specify the max lenght of an email. We also specify that email must be unique.
    name = models.CharField(max_lenght = 255)                                   # The name filed will contain email names.
    is_active = models.BooleanField(default = True)                             # 1st field for permission system - determines if the user is active (by default we have set that for true).
    is_staff = models.BoleanField(default = False)                              # 2nd field for permission system - determines if the user is a staff (has access to the Django admin, etc.).

    objects = UserProfileManager()                                              # We need to specify the model manager that we are going to use for the objects. This is required because
                                                                                # we need to use our custom user model with the Django CLI. So Django needs to have a custom model manager
                                                                                # for the user model so it knows how to create users and control users using the Django command line tools.
                                                                                # UserProfileManager isn created yet - it will but later.

                                                                                # To work with Django admin and the Django authentication system.
    USERNAME_FIELD = "email"                                                    # To override default username field and replace it with email field so this means that when we
                                                                                # authenticate users instead of them providing a username and password they are just going to provithe
                                                                                # their email address and password.
    REQUIRED_FIELDS = ["name"]                                                  #

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
