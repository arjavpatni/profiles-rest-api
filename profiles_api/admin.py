from django.contrib import admin
from profiles_api import models

# Register your models here to be controlled by Django admin.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
