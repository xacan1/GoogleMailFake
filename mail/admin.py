from django.contrib import admin
from mail.models import Email


class EmailAdmin(admin.ModelAdmin):
    model = Email
    list_display = ('user', 'sender', 'subject',
                    'timestamp', 'read', 'archived',)
    list_filter = ('read', 'archived',)
    list_editable = ('read', 'archived',)
    list_display_links = ('user',)
    search_fields = ('user', 'sender', 'subject',)


admin.site.register(Email, EmailAdmin)
