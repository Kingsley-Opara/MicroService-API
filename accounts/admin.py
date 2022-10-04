from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .forms import AdminChangeForm

# Register your models here.

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    model = User
    search_fields = ['username', 'email', 'unique_id']
    ordering = ['created']
    list_display = ['email', 'unique_id']
    list_filter = ['is_staff', 'is_superuser']

    form = AdminChangeForm

    fieldsets = (
        (None, {'fields': (['email'])}),
        ('Personal info', {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
        'classes': ('wide',),
        'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

admin.site.register(User, UserAdmin)