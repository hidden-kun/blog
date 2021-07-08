from django.http import response
from post.models import Category, Post
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Post
    template_name ='post/index.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs )
        post = self.object 
        post.views =post.views + 1 
        post.save()
        return response
        
    
class PostByCategory(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'


    def  get_queryset(self):
        category_slug = self.kwargs.get('slug')
        posts = Post.objects.filter(category__slug=category_slug)
        return posts 
        



