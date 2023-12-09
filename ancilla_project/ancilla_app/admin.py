from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import StaffUser


class StaffUserAdmin(UserAdmin):
    model = StaffUser


admin.site.register(StaffUser, StaffUserAdmin)
