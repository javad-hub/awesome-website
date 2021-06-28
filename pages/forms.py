from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')


choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'category', 'text')

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type the theme here...'}),
			'author':forms.Select(attrs={'class':'form-control'}),
			'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
			'text':forms.Textarea(attrs={'class':'form-control','placeholder':'What is the awesome story!!!'}),


		}



class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text')

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type the theme here...'}),
			#'author':forms.Select(attrs={'class':'form-control'}),
			'text':forms.Textarea(attrs={'class':'form-control','placeholder':'What is the awesome story!!!'}),


		}