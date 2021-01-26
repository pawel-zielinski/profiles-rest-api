from django.contrib import admin
from profiles_api import models                                                 # Import models from our project


admin.site.register(models.UserProfile)                                         # To tell the Django admin to register our user profile model with the admin site so it makes it
                                                                                # accessible through the admin interface.
# Register your models here.
