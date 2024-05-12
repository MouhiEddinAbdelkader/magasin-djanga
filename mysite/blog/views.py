from .models import Post
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .forms import PostForm
from django.urls import reverse_lazy


def Posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    context_object_name = 'post'
    
class CreerPost(CreateView):
   model = Post
   template_name = 'blog/creer_post.html'
   form_class = PostForm   
   success_url = reverse_lazy('blog/posts')