from django.shortcuts import render
from myblog.models import Post, Author
 
def index(request):
    all_posts = Post.objects.all().order_by('-date')
    template_data = {'posts' : all_posts}
 
    return render_to_response('blog.html', template_data)