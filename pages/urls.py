from django.urls import path
from .views import HomeView, DetailView, AddView, PostUpdateView, PostDeleteView

urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('post/<int:pk>', DetailView.as_view(), name="post-detail"),
	path('add-post/', AddView.as_view(), name="add-post"),
	path('update-post/<int:pk>', PostUpdateView.as_view(), name="post-update"),
	path('delete-post/<int:pk>', PostDeleteView.as_view(), name="post-delete"),
]