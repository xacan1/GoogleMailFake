from django.contrib import admin
from mail.models import Email, Category, Attachment


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class EmailAdmin(admin.ModelAdmin):
    model = Email
    list_display = ('user', 'display_name', 'category__name', 'sender', 'subject',
                    'parent', 'timestamp', 'read', 'archived',)
    list_filter = ('read', 'archived',)
    list_editable = ('read', 'archived',)
    list_display_links = ('user',)
    search_fields = ('user', 'sender', 'subject', 'category__name',)


class AttachmentAdmin(admin.ModelAdmin):
    model = Attachment
    list_display = ('email', 'file',)
    list_display_links = ('email', 'file',)
    search_fields = ('email__user__email', 'file',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Attachment, AttachmentAdmin)
