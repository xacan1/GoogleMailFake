from django import forms
from mail.models import *


class SimpleForm(forms.Form):
    pass


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file']


class AddMailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['user', 'category', 'sender',
                  'recipients', 'subject', 'body', 'parent']
        widgets = {
            'user': forms.Select(attrs={'hidden': ''}),
            'parent': forms.Select(attrs={'hidden': ''}),
            'category': forms.Select(attrs={'class': 'form-select w-25'}),
            'sender': forms.TextInput(attrs={'placeholder': 'Отправитель', 'class': 'new__who-input'}),
            'recipients': forms.TextInput(attrs={'placeholder': 'Получатель', 'class': 'new__who-input'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Тема', 'class': 'new__input-title'}),
            'body': forms.Textarea(attrs={'cols': 60, 'rows': 14, 'class': 'w-100 new__input-textarea'}),
        }


AddFilesFromSet = forms.inlineformset_factory(Email, Attachment,
                                              form=AttachmentForm, extra=5,
                                              can_delete=False)
