from django.contrib import admin
from authy.models import Profile, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


# to clean up inactive users or activation error
# from .models import User
# from django.utils import timezone
# from datetime import timedelta
# from django.conf import settings
# User.objects.filter(
# is_active=False,
# date_joined__lt=timezone.now() -
# timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
# ).delete()

admin.site.register(User, UserAdmin)
admin.site.register(Profile)