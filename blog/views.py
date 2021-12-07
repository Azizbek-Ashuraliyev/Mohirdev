from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse_lazy


class BlogListView(generic.ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(generic.edit.CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','body']

class BlogEditView(generic.edit.UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(generic.edit.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')