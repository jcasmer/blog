

from django.db import models


class CustomManager(models.Manager):
    '''
    Clase para realizar las consultas filtrandolas por el deleted
    Esto debido a que se está eliminando lógicamente los registros
    '''

    def get_queryset(self):
        
        return super().get_queryset().filter(deleted=False)