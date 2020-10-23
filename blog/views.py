from django.shortcuts import render, get_object_or_404, Http404, redirect,reverse
from . import forms
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib import messages
from django.core.paginator import Paginator, Page
# Create your views here.
@login_required
def create_post(request):
    if request.method == 'POST':
        form = forms.PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'your post is created.')
            return redirect(reverse('blog:display_posts'))
    else:
        form = forms.PostCreationForm()
    return render(request, 'blog/create_post.html',{'form':form})

def display_posts(request):
    posts = models.Post.objects.all().order_by('-date_posted')
    paginator = Paginator(posts,3)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'blog/display_posts.html',{'page_obj':page_obj})

@login_required
def display_my_posts(request):
    posts = models.Post.objects.filter(author=request.user).order_by('-date_posted')
    paginator = Paginator(posts,3)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'blog/display_posts.html',{'page_obj':page_obj})

def display_post(request, id):
    try :
        post = models.Post.objects.get(pk=id)
    except models.Post.DoesNotExist:
        raise Http404()
    is_liked = False
    # get total likes to post
    likes_count = post.get_total_likes()
    # if current post is liked by
    if post.likedby.filter(id=request.user.id).exists():
        is_liked = True
    comments = post.comments.all()
    return render(request, 'blog/display_post.html',
                  {'post':post,'comments':comments,
                   'is_liked':is_liked,
                   'likes_count':likes_count})

@login_required
def delete_post(request, id):
    try:
        post = models.Post.objects.get(pk=id)
    except models.Post.DoesNotExist:
        raise Http404()
    if request.user == post.author:
        post.delete()
        messages.success(request,'Post '+str(post.title)+' is deleted.')
        return redirect(reverse('blog:display_posts'))
    else:
        messages.warning(request, 'you can not delete this post, since you are not the owner')
        return redirect(reverse('blog:display_post', args=[id]))


@login_required
def edit_post(request, id):
    try:
        post = models.Post.objects.get(pk=id)
    except models.Post.DoesNotExist:
        raise Http404()

    # checking the ownership
    if request.user != post.author:
        messages.warning(request, 'you can not edit this post, since you are not the owner')
        return redirect(reverse('blog:display_post', args=[id]))

    # post.author = request.user.username
    if request.method == 'POST':
        form = forms.PostEditForm(request.POST, instance=post)
        if form.is_valid():
            print(form.cleaned_data)
            form.cleaned_data['author'] = request.user.username
            form.save()
            messages.success(request, 'Post ' + str(form.cleaned_data['title']) + ' is updated.')
            return redirect(reverse('blog:display_posts'))
    else:
        form = forms.PostEditForm(initial={'title' : post.title, 'content':post.content})
    return render(request,'blog/edit_post.html',{'form':form})

@login_required
def add_comment(request,post_id):
    if request.method == 'POST':

        # comment = models.Comment.objects.create()
        form = forms.CommentCreationForm(request.POST or None)
        post = get_object_or_404(models.Post, pk = post_id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.commenter = request.user
            comment.save()
            messages.success(request,'your comment added...')
            return redirect(reverse('blog:display_post',args=[post_id]))
    else:
        form = forms.CommentCreationForm()
    return render(request,'blog/add_comment.html', {'form':form})

@login_required
def delete_comment(request, post_id, comment_id):
    try:
        comment = models.Comment.objects.get(pk=comment_id)
    except models.Post.DoesNotExist:
        raise Http404()
    if comment.commenter == request.user:
        comment.delete()
        messages.success(request,'your comment is deleted.')
        return redirect(reverse('blog:display_post',args=[post_id]))
    else:
        messages.warning(request, 'you can not delete others comments')
        return redirect(reverse('blog:display_post', args=[post_id]))

@login_required
def edit_comment(request, post_id, comment_id):

    try:
        comment = models.Comment.objects.get(pk=comment_id)
    except models.Post.DoesNotExist:
        raise Http404()
    # post.author = request.user.username


    #checking ownership
    if request.user != comment.commenter:
        messages.warning(request, 'this is not your comment')
        return redirect(reverse('blog:display_post',args=[post_id]))

    if request.method == 'POST':
        form = forms.CommentEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.cleaned_data['author'] = request.user.username
            form.save()
            messages.success(request, 'your comment is updated.')
            return redirect(reverse('blog:display_post',args=[post_id]))
    else:
        form = forms.CommentEditForm(initial={'comment' : comment.comment})
    return render(request,'blog/edit_comment.html',{'form':form})

def like_post(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    is_liked = False
    if request.method == 'POST':
        post.likedby.add(request.user)
        post.save()
        is_liked = True
    return redirect(reverse('blog:display_post', args=[post_id]),kwargs={'is_liked':is_liked})
    # post = models.Post.objects.get()

def dislike_post(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    is_liked = True
    if request.method == 'POST':
        post.likedby.remove(request.user)
        post.save()
        is_liked = False
    return redirect(reverse('blog:display_post', args=[post_id]),kwargs={'is_liked':is_liked})








