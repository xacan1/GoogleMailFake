from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import *



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'last_name', 'first_name',
                    'last_login', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    list_editable = ('is_staff', 'is_active',)
    list_display_links = ('email', 'last_name', 'first_name',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name',
                           'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name',
                       'is_staff', 'is_active',)}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)