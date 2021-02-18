from django.contrib import admin
from profiles_api import models                                                 # Import models from our project


admin.site.register(models.UserProfile)                                         # To tell the Django admin to register our UserProfile model with the admin site so it makes it
                                                                                # accessible through the admin interface.
admin.site.register(models.ProfileFeedItem)
# Register your models here.
