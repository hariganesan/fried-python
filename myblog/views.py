from django.shortcuts import render
from myblog.models import Post, Tag
 
def page(request, num="1"):
    all_posts = Post.objects.all().order_by('-date')
    template_data = {'posts': all_posts}
 
    return render(request, 'blog.html', template_data)