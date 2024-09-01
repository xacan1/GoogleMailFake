from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone(value):
    if len(value) != 11 or not value.isdigit() or value[0] != '7':
        raise ValidationError('Введите правильный мобильный номер(только цифры) начинающийся на 7')
