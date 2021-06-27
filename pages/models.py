from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=220)
	title_tag = models.CharField(max_length=220)
	author = models.ForeignKey(User , on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateField(auto_now_add=True)


	def __str__(self):
		return self.title + ' | ' + str(self.author)


	def get_absolute_url(self):
		return reverse('post-detail', args=(str(self.id)))

