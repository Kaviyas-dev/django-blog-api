from django.shortcuts import render
from blogapp.models import Profile,Post,Comments
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
class PostView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'home'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class AddPost(LoginRequiredMixin,CreateView):
    model = Post
    fields=["title","description"]
    template_name='add_post.html'
    success_url=reverse_lazy('home')

    login_url = "login"

    def form_valid(self, form):

        form.instance.author = self.request.user

        return super().form_valid(form)

    
class UpdatePost(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields=["title","description"]
    template_name='update_post.html'
    success_url=reverse_lazy('home')

    login_url = "login"

    def test_func(self):

        post = self.get_object()

        return post.author == self.request.user

class DeletePost(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name='delete_post.html'
    context_object_name='home'
    success_url=reverse_lazy('home')

    login_url = "login"

    def test_func(self):

        post = self.get_object()

        return post.author == self.request.user





