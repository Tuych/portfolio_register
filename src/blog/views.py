from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogs(request):
    blogs = Blog.objects.order_by('-date')  # data ni usish tartibida chiqaradi 2-yul, 5-iyul
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
