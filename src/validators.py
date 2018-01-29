'''
Django custom validations
'''
from django.core.validators import RegexValidator


IS_ALPHAVALIDATOR = RegexValidator(r'^[a-zA-Z-ñÑ-áéíóúÁÉÍÓÚ ]+$',
                                   message='Este campo sólo permite letras.',
                                   code='Inválido')
