from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts.forms import AddCommentForm, AddPostForm,EditPostForm,AddReplyForm
from django.shortcuts import get_object_or_404, render,redirect
from .models import Comment, Post, Vote
from django.utils.text import slugify
from django.contrib import messages

def all_posts(request):

    posts=Post.objects.all()
    
    context={'posts':posts}

    return render(request,'posts/all_posts.html',context)


def post_detail(request,year,month,day,slug):

    post=get_object_or_404(Post, created__year=year, created__month=month, created__day=day, slug=slug)
    comments=Comment.objects.filter(post=post, is_reply=False)
    reply=AddReplyForm()
    can_like=False
    if request.user.is_authenticated:
        if post.user_can_like(request.user):
            can_like=True

    if request.method=="POST": 
        form=AddCommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.user=request.user
            new_comment.save()
            messages.success(request,'your comment submitted SUCCESSFULLY','success')
    else:
        form=AddCommentForm()



    return render(request,'posts/post_detail.html',{'post':post,'comments':comments,'form':form,'reply':reply,'can_like':can_like})
@login_required
def add_post(request,user_id):
    if request.user.id==user_id:
        if request.method=="POST":
            form=AddPostForm(request.POST)
            if form.is_valid():
                new_post=form.save(commit=False)
                new_post.user=request.user
                new_post.slug=slugify(form.cleaned_data['body'][:30])
                new_post.save()
                messages.success(request, "Your post submitted",'success')
                return redirect("account:dashboard", user_id)


        else:

                form=AddPostForm()
        context={'form':form}
        return render(request,'posts/add_post.html',context)
    else:
        return redirect('posts:all_posts')


@login_required
def post_delete(request,user_id,post_id):
    if request.user.id==user_id:
        Post.objects.filter(pk=post_id).delete()
        messages.success(request,"YOur Post deleted",'success')
        return redirect('account:dashboard',user_id)
    else:

        return redirect('posts:all_posts')        

@login_required
def post_edit(request,user_id,post_id):
    if request.user.id==user_id:
        post=get_object_or_404(Post, pk=post_id)
        if request.method=='POST':
            form=EditPostForm(request.POST,instance=post)
            if form.is_valid():
                ep=form.save(commit=False)
                ep.slug=slugify(form.cleaned_data['body'][:30])
                ep.save()
                messages.success(request,'Your Post edited Successfully','success')
                return redirect('account:dashboard', user_id)

        else:
            form=EditPostForm(instance=post)
        return render(request,'posts/edit_post.html',{'form':form })
    
    else:

     return redirect('posts:all_posts')



@login_required
def add_reply(request,post_id,comment_id):
    post=get_object_or_404(Post, id=post_id)
    comment=get_object_or_404(Comment,pk=comment_id)
    if request.method=="POST":
        form=AddReplyForm(request.POST)
        if form.is_valid():
            reply=form.save(commit=False)
            reply.user=request.user
            reply.post=post
            reply.comment=comment
            reply.is_reply=True
            reply.save()
            messages.success(request,'Your reply submitted Successfully','success')
    return redirect('posts:post_detail', post.created.year, post.created.month, post.created.day, post.slug)





@login_required  
def post_like(request,post_id):
    
    post=get_object_or_404(Post, id=post_id)
    like=Vote(post=post, user=request.user)
    like.save()
    messages.success(request, 'you liked successfully','success')
    return redirect('posts:post_detail', post.created.year, post.created.month, post.created.day, post.slug)