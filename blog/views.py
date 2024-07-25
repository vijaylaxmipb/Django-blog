from django.shortcuts import render
from django.http import HttpResponse

# Ensure this function or class exists
def my_blog(request):
    return render(request, 'blog/my_blog.html')