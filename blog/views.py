from django.shortcuts import render
import os

from .models import Post

def posts_list(request):
    count = 1
    #if request.method == "GET": кол-во просмотров статьи
    #    views_n = open("page_views.txt", 'r')
    #    a = views_n.read()
    #    count = int(a)
    #    count += 1
    #    views_n.seek(0)
    #    views_n.close()
    #    views_n = open("page_views.txt", 'w')
    #    views_n.write(str(count))
    #    views_n.close()
        # <a>
        #   <center>{{ audience }}</center>
        # </a>
    posts = Post.objects.all()
    return render(request, "blog/index.html", context={'posts': posts, 'audience': count})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})
