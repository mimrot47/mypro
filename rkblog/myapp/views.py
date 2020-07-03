from django.shortcuts import render,get_object_or_404
from myapp.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailSendForm
from django.core.mail import send_mail

# Create your views here.
from taggit.models import Tag
def home(Request,tag_slug=None):
    Post_list=Post.objects.all().order_by('-publish')
    Post_list1=Post.objects.all().order_by('-publish')
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        Post_list.filter(tags__in=[tag])
    pagenator=Paginator(Post_list,2)
    page_number=Request.GET.get('page')
    try:
        Post_list=pagenator.page(page_number)
    except PageNotAnInteger:
        Post_list=pagenator.page(1)
    except EmptyPage:
        Post_list=pagenator.page(pagenator.num_pages)
    MY_DIST={'post_list':Post_list,'post_list1':Post_list1,'tag':tag}
    return render(Request,'myapp/index.html',MY_DIST)


def Email_send_view(Request,id):
    form=EmailSendForm()
    post=Post.objects.get(id=id)
    send=False
    if Request.method=='POST':
        form=EmailSendForm(Request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            email=cd['email']
            name=cd['name']
            to=[cd['to']]
            comment=cd['comments']
            # send_mail(name,email,'vigosoftpvt@gmail.com',to)
            send=True
            print(name,email,to,comment)
        else:
            print('mail not send')
        
    MY_DICT={'form':form,'post':post}
    return render(Request,'myapp/EmailForm.html',MY_DICT)


from myapp.forms import commentForm
def post_detail(Request,pk):
    post=Post.objects.get(id=pk)
    comments=post.comment.filter(active=True)
    csubmit=False
    if Request.method=="POST":
        form=commentForm(Request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else: 
        form=commentForm()

    MY_DICT={'post':post,'form':form,'comment':comments,'cs':csubmit}

    return render(Request,'myapp/details_post.html',MY_DICT)
    