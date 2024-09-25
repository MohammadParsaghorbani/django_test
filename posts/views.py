from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Comments

# Create your views here.
def index(request):
    return HttpResponse("<h1>welcom</h1>")

def home(request):
    return render(request, 'index.html')
    #return HttpResponse('<h1>parsa</h1>')

def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request,'post_list.html',context=context)

def post_detail(request,pk):
    post = Post.objects.get(pk = pk)
    comments = Comments.objects.filter(post=post)
    context = {'post':post,'comments' : comments}
    return render(request,'post_details.html',context=context)
