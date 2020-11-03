from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', context={'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5





class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created_at')

    # def get_contex_data(self,*args,**kwargs):
    #     context = super(UserPostListView, self).get_contex_data(*args,**kwargs)
    #     context['likes'] = Like.objects.filter(liker=self.kwargs.get('username'),
    #                                         post=self.get)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


def about(request):
    context = {'paragraph': 'Knowledge sharing road...'}
    return render(request, 'blog/about.html', context=context)

@login_required
def like(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        post = Post.objects.get(id=post_id)
        existing = Like.objects.filter(liker=user, post=post).exists()
        if existing:
            instance = Like.objects.get(liker=user, post=post)
            if instance.value == 'like':
                instance.value = 'unlike'
                instance.save()
            else:
                instance.value = 'like'
                instance.save()
        else:
            Like.objects.create(liker=user, post=post, value='like')
    return redirect(reverse('home'))
