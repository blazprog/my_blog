from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/articles.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/article_tabs.html', {"post": post, 'active_tab': 'post'})


def post_detail_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/article_tabs.html', {"post": post, 'active_tab': 'comment'})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print ("In post edit")
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            print ('form is valid')
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            print ('Post saved')
            return redirect('post_detail', pk=post.pk)
        else:
            print('errors by saving')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/article_edit.html', {'form': form, 'post': post})


@login_required
def comment_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print (post.title)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            print('Errors by saving form', form.errors)
    else:
        form = CommentForm(instance=post)
    return render(request, 'blog/comment_edit.html', {'form': form, 'post': post})
