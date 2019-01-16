from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse

from .forms import PostCreationForm
from .models import Post


def new_page(request):
    if request.method == 'GET':
        form = PostCreationForm()
    else:
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'post/post_new.html', {'form': form})


class PostDetailView(DetailView):
    model = Post


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        form = PostCreationForm(instance=post)
    else:
        form = PostCreationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse('post:detail', kwargs={'pk': post.pk}))

    return render(request, 'post/post_update.html', {'form': form, 'post': post })
