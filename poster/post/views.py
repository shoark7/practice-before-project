from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


class PostList(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'post_list.html'


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})


class PostDetail(DetailView):
    template_name = 'post_detail.html'
    model = Post


