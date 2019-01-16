from django import forms
from django.forms import ModelForm

from post.models import Post


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
