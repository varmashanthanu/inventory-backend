from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('role', 'is_active', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("role", "phone_number")}),)


admin.site.register(User, UserAdmin)
