from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'digcomp_level', 'is_staff', 'is_active')
    list_filter = ('role', 'digcomp_level', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Platform Details', {'fields': ('role', 'bio', 'avatar', 'digcomp_level')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Platform Details', {'fields': ('role', 'bio', 'avatar', 'digcomp_level')}),
    )
