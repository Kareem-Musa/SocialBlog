from django.shortcuts import render
from .models import Post
from .forms import PostForm

def blog(request):
    return render(request,'blog/blogs.html')

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render('blog:blogs')
    else :
        form = PostForm()
    return render(request,'blog/create_post.html',{'form':form})
