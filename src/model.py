
import datetime

from django.db import models
from django.contrib.auth.models import User

from src.manager import CustomManager


class BaseModel(models.Model):
    '''
    Modelo base
    '''

    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField(
        'Fecha de modificación', null=True)    
    deleted = models.BooleanField('Eliminado', default=False)

    objects = CustomManager()

    def delete(self):
        '''
        Sobreescribimos el método de eliminación para que el borrado sea lógico y no fisico
        por este motivo se realiza un update
        '''
        self.deleted = True
        self.save()

  
    class Meta:
        abstract = True