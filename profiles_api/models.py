from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

#CUSTOM USER MANAGER
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password = None):                        # This is what the Django CLI will use when creating users with the command line tool. (password = None -
        """Create a new user profile"""                                         # because of the way the Django password checking system works [a non-password will not work because it
                                                                                # needs to be a hash so basically untill you set a password you will not be able to authenticate with the user]).
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)                                     # Makes given email key sensitive (lower or upper case) only for secound half of an email.
        user = self.model(email = email, name = name)                           # It creates a new model that the user manager is representing. So by default self.model is set to the model
                                                                                # that the manager is for and then it will create a new model object and set the email and the name.
        user.set_password(password)                                             # To encrypt the password.
        user.save(using = self._db)                                             # To save user model. The best practice is to add this line just to make sure that we support a multiple databases.

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user


#CLASS FOR MODELS
class UserProfile(AbstractBaseUser, PermissionsMixin):                          # Inheritance from AbstractBaseUser and PermissionsMixin allows us to base our abstract user model
    """Database model for users in the system"""                                # on default Django user model.
    email = models.EmailField(max_length = 255, unique = True)                  # With every EmailField we specify the max lenght of an email. We also specify that email must be unique.
    name = models.CharField(max_length = 255)                                   # The name filed will contain email names.
    is_active = models.BooleanField(default = True)                             # 1st field for permission system - determines if the user is active (by default we have set that for true).
    is_staff = models.BooleanField(default = False)                             # 2nd field for permission system - determines if the user is a staff (has access to the Django admin, etc.).

    objects = UserProfileManager()                                              # We need to specify the model manager that we are going to use for the objects. This is required because
                                                                                # we need to use our custom user model with the Django CLI. So Django needs to have a custom model manager
                                                                                # for the user model so it knows how to create users and control users using the Django command line tools.
                                                                                # UserProfileManager isn created yet - it will but later.

                                                                                # To work with Django admin and the Django authentication system.
    USERNAME_FIELD = 'email'                                                    # To override default username field and replace it with email field so this means that when we
                                                                                # authenticate users instead of them providing a username and password they are just going to provithe
                                                                                # their email address and password.
    REQUIRED_FIELDS = ['name']                                                  # This specifies additional required fields (at a minimum the user must specify their email address and their name)

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):                                                          # Recommended for all Django models because otherwise when you convert it to a string it will not necessarily
        """Return string representation of our user"""                          # be a meaningfull output.
        return self.email
