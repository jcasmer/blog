# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic import View

from post.models import PostBlog, Comment
from post.forms import PostForm


class HomeView(View):
    '''
    '''
    template_name = 'blog/index.html'

    def get(self, request):
        '''
        Método get
        '''
        data = PostBlog.objects.all().order_by('-created_at')
        output = {
            'results': data,
        }
        return render(request, self.template_name, output)


class PostView (View):

    template_name = 'blog/post/post.html'

    def get(self, request, *args, **kwargs):
        """
        Muestra el formulario 
        """
        form = PostForm()
        output = {
            'form': form,
        }
        return render(request, self.template_name, output)


    def post(self, request, *args, **kwargs):
        """
        Muestra el formulario 
        """
        form = PostForm(request.POST)
        if not form.is_valid():
            messages.error(request, 'Valide los errores')
            output = {
                'form': form,
            }
            return render(request, self.template_name, output)
        
        form.save()
        messages.success(request, 'Post registrado exitosamente')        
        return HttpResponseRedirect(reverse('post:index'))


class EditPostVIew(View):

    template_name = 'blog/post/edit.html'

    def get(self, request, *args, **kwargs):
        """
        Muestra el formulario 
        """
        if not kwargs['id']:
            messages.error(request, 'Post no encontrado')        
            return HttpResponseRedirect(reverse('post:index'))
        
        post = PostBlog.objects.get(id=kwargs['id'])
        form = PostForm(instance=post)        
        output = {
            'form': form,

        }
        return render(request, self.template_name, output)


    def post(self, request, *args, **kwargs):
        """
        Muestra el formulario 
        """
        post = PostBlog.objects.get(id=kwargs['id'])
        form = PostForm(request.POST, instance=post)
        if not form.is_valid():
            messages.error(request, 'Valide los errores')
            output = {
                'form': form,

            }
            return render(request, self.template_name, output)
        
        form.save()
        messages.success(request, 'Post actualizado exitosamente')        
        return HttpResponseRedirect(reverse('post:index'))

class DeletePostView(View):

    template_name = 'blog/post/delete.html'

    def get(self, request, *args, **kwargs):
        """
        Muestra el formulario 
        """
        if not kwargs['id']:
            messages.error(request, 'Post no encontrado')   
            return HttpResponseRedirect(reverse('post:index'))    
        output = {
            'id': kwargs['id'],
        }
        return render(request, self.template_name, output)


    def post(self, request, *args, **kwargs):
        """
        ELimina el post
        """        
        if not request.POST.get('id-delete'):
            messages.error(request, 'Post no encontrado')       
            return HttpResponseRedirect(reverse('post:index'))
        
        post = PostBlog.objects.get(id=request.POST.get('id-delete'))
        # se elimina lógicamente desde el src.model.py método delete
        post.delete()
        comments = Comment.objects.filter(post_blog=request.POST.get('id-delete'))
        if comments:
            for comment in comments:
                comment.delete()

        messages.success(request, 'Post eliminado exitosamente')        
        return HttpResponseRedirect(reverse('post:index'))