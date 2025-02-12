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
                             related_name='emails',
                             verbose_name='Пользователь')
    category = models.ForeignKey(Category, blank=True, null=True,
                                 on_delete=models.CASCADE,
                                 related_name='emails_category',
                                 verbose_name='Категория')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, default=None,
                               null=True, blank=True, related_name='parent_email',
                               verbose_name='Родительское письмо')
    display_name = models.CharField(max_length=255, default='', blank=True,
                                    verbose_name='Представление')
    sender = models.CharField(max_length=255, default='', blank=True,
                              verbose_name='Отправитель')
    recipients = models.CharField(max_length=4096, verbose_name='Получатель')
    subject = models.CharField(max_length=255, verbose_name='Тема')
    body = models.TextField(blank=True, default='', verbose_name='Тело письма')
    timestamp = models.DateTimeField(auto_now_add=True,
                                     verbose_name='Дата письма')
    read = models.BooleanField(default=False, verbose_name='Прочитано')
    archived = models.BooleanField(default=False,
                                   verbose_name='Заархивировано')

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
        ordering = ['-timestamp']
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Attachment(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE,
                              related_name='get_attachments', verbose_name='Письмо')
    file = models.FileField(upload_to='attachments/', null=True,
                            blank=True, verbose_name='Вложение')
    
    def __str__(self) -> str:
        return self.file.name
    
    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
