# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from post.models import PostBlog, Comment


class PostForm(ModelForm):
                    
            
    class Meta:

        '''
        Contiene el modelo que necesita el template
        '''
        model = PostBlog
        fields = ['title', 'body']

class CommentForm(ModelForm):

    class Meta:
        
        '''
        Contiene el modelo que necesita el template
        '''
        model = Comment
        fields = ['post_blog', 'commentary', 'name']

