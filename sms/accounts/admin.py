from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(User)
class UserAdminConfig(UserAdmin):
    ordering = ("-timestamp",)
    list_display = ("email", "user_name", "first_name",
                    "last_name", "type_of_user", "is_active", "is_staff")

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'type_of_user')}),
        ('Permission', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('last_name',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'type_of_user', 'is_active', 'is_staff')
        }),
    )
