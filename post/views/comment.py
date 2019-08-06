# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic import View

from post.models import PostBlog, Comment
from post.forms import CommentForm

class CommentListView(View):

    template_name = 'blog/comment/list.html'

    def get_post(self, id_post):

        try:
            post = PostBlog.objects.get(id=id_post)   
        except PostBlog.DoesNotExist:
            post = None
        return post

    def get_commentary(self, id_post):

        try:
            comments = Comment.objects.filter(post_blog=id_post).order_by('-created_at')  
        except Comment.DoesNotExist:
            comments = None
        return comments

    def get(self, request, *args, **kwargs):
        """
        Muestra el formulario 
        """
        if not kwargs['id']:
            messages.error(request, 'Post no encontrado')        
            return HttpResponseRedirect(reverse('post:index'))  
        
        post = self.get_post(kwargs['id']) 
        if not post:
            messages.error(request, 'Post no encontrado')        
            return HttpResponseRedirect(reverse('post:index'))
        comments = self.get_commentary(kwargs['id'])

        form_comment = CommentForm(initial={'post_blog':kwargs['id']})
        output = {
            'post': post,
            'form': form_comment,
            'comments': comments, 
        }
        return render(request, self.template_name, output)


    def post(self, request, *args, **kwargs):
        """
        Muestra el formulario 
        """
        form = CommentForm(request.POST)
        if not form.is_valid():
            post = self.get_post(kwargs['id']) 
            comments = self.get_commentary(kwargs['id'])
            messages.error(request, 'Valide los errores')
            output = {
                'post': post,
                'form': form,
                'comments': comments,
            }
            return render(request, self.template_name, output)
        
        form.save()
        messages.success(request, 'Comentario registrado exitosamente')        
        return HttpResponseRedirect(reverse('post:list', kwargs={'id':kwargs['id']}))