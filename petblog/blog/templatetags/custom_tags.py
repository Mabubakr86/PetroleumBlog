from django import template 
from ..models import Post, Like 


register = template.Library() 
@register.simple_tag 
def get_last_like_status(post,user): 
     if Like.objects.filter(post=post,liker=user).exists():
        last = Like.objects.get(post=post,liker=user).value
        return last == 'like'
