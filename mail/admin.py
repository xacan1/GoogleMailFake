from django.contrib import admin
from mail.models import Email, Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class EmailAdmin(admin.ModelAdmin):
    model = Email
    list_display = ('user', 'category__name', 'sender', 'subject',
                    'timestamp', 'read', 'archived',)
    list_filter = ('read', 'archived',)
    list_editable = ('read', 'archived',)
    list_display_links = ('user',)
    search_fields = ('user', 'sender', 'subject', 'category__name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Email, EmailAdmin)
