from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Email(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='emails')
    category = models.ForeignKey(Category, blank=True, null=True,
                                 on_delete=models.CASCADE,
                                 related_name='emails_category')
    sender = models.CharField(max_length=255, default='')
    recipients = models.CharField(max_length=4096)
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user.email} - {self.subject}'

    def get_absolute_url(self) -> str:
        return reverse('mail-body', kwargs={'email_pk': self.pk})

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'sender': self.sender,
            'recipients': self.recipients,
            # "recipients": [email_addr.strip() for email_addr in self.recipients.split(',')],
            'subject': self.subject,
            'body': self.body,
            'timestamp': self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            'read': self.read,
            'archived': self.archived
        }

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
