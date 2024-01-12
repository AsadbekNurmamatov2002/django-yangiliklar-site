from django.shortcuts import render, redirect ,get_object_or_404
from django.db.models import Q
from .models import Post, PostName, Message
# from django.urls import reverse

def Home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    post=Post.objects.filter(Q(title__icontains=q)|
                             Q(postname__name__icontains=q)|
                             Q(body__icontains=q))
    postname=PostName.objects.all()
    context={'post':post, 'postname':postname}
    return render(request, 'index.html',context)

def post_ditile(request, year, month, day, slug):
    post=get_object_or_404(Post, publish__year=year, publish__month=month, publish__day=day, slug=slug)
    if request.method=='POST':
        if request.user.is_authenticated:
            body=request.POST.get('body') if request.POST.get('body')!=None else ''
            message=Message.objects.create(
                auther=request.user,
                post=post,
                Mbody=body
            )
            return redirect('myapp:postditile', year=post.publish.year, month=post.publish.month, day=post.publish.day, slug=post.slug )
        else:
            return redirect('loginpage')
    coments=post.message_set.all()
    # post
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    posts=Post.objects.filter(Q(title__icontains=q)|
                             Q(postname__name__icontains=q)|
                             Q(body__icontains=q))
    postname=PostName.objects.all()
    context={'post':post, 'postname':postname, 'coments': coments, 'posts':posts}
    return render(request, 'post_ditile.html', context)