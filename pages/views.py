from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.



def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-date']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
	    total_likes = stuff.total_likes()
	    context["total_likes"] = total_likes
		return context


def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-',' '))
	return render(request, 'categories.html', {'cats':cats.replace('-',' '), 'category_posts':category_posts})


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