from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import StaffUser, Patron, Book, Checkout, Hold


class StaffUserAdmin(UserAdmin):
    model = StaffUser


admin.site.register(StaffUser, StaffUserAdmin)
admin.site.register(Patron)
admin.site.register(Book)
admin.site.register(Checkout)
admin.site.register(Hold)
