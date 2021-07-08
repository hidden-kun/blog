from django import template
from post.models import Post, Tag

register = template.Library()

@register.inclusion_tag('post/popular_posts_tpl.html')
def get_popular(amount=3, category= None):
    posts = Post.objects.order_by('-views')
    if category is not None :
        posts = posts.filter(category=category)
    posts = posts[:amount]
    return {'posts': posts}


@register.inclusion_tag('post/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}