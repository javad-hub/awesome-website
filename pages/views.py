from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-date']

class DetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class AddView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'

class PostUpdateView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'

class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy('home')
	template_name = 'delete_post.html'