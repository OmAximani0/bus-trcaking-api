from django.contrib import admin
from users.models import Users
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django import forms


class UserAdminConfig(UserAdmin):
    model = Users
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    search_fields = ('fullname','email')
    list_filter = ('fullname','is_active','is_staff' )
    list_display = ('fullname', 'is_active','is_staff' )
    fieldsets = (
        (None, {'fields': ('fullname','password','email')}),
        ('Permissions', {'fields': ('is_active','is_staff')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('fullname','email','password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    ordering = ('fullname','email')


admin.site.register(Users, UserAdminConfig)