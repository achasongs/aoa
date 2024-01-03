from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

# Create your views here.
class BlogHome(ListView):
    model = Post
    template_name = 'blog/bloghome.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    # fields =['title', 'title_tag', 'body']