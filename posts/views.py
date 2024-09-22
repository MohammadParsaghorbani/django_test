from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    return HttpResponse("<h1>welcom</h1>")

def home(request):
    return HttpResponse("<h1>welcome</h1>")


def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request,'posts/post_list.html',context=context)

def post_detail(request,pk):
    post = Post.objects.get(pk = pk)
    context = {'post':post}
    return render(request,'posts/post_detail.html',context=context)
