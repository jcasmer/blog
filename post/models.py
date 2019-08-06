

from django.db import models
from django.contrib.auth.models import User

from src.model import BaseModel
from src.validators import IS_ALPHAVALIDATOR

# Create your models here.

class PostBlog(BaseModel):
    
    title = models.CharField('Título',max_length=200)
    body = models.TextField('Texto del post')

    def __str__(self):
        return self.title


class Comment(BaseModel):

    post_blog = models.ForeignKey(PostBlog, verbose_name='Post',on_delete=models.CASCADE )
    commentary = models.TextField('Comentario', max_length=500)
    name = models.CharField('Nombre', max_length=150, validators=[IS_ALPHAVALIDATOR])
    
    def __str__(self):
        return self.commentary
