from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.urls import reverse
from .form import FormBlog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

from .models import BlogPost


def check_blog_owner(obj, request):
    if obj.owner != request.user:
        raise Http404


def index(request):
    Blogs = BlogPost.objects.order_by('-date_added')
    context = {'Blogs': Blogs}
    return render(request, 'blogs/index.html', context)


def user_page(request, ownerid, ownername):
    Blogs = BlogPost.objects.filter(owner_id=ownerid).order_by('-date_added')
    owner = ownername
    context = {'Blogs': Blogs, 'owner': owner}
    return render(request, 'blogs/userpage.html', context)


@login_required
def personal_index(request, user_id):
    if user_id != request.user.id:
        raise Http404
    Blogs = BlogPost.objects.filter(owner_id=user_id).order_by('-date_added')
    owner = request.user
    context = {'Blogs': Blogs, 'owner': owner}
    return render(request, 'blogs/personal.html', context)


@login_required
def personal_new_blog(request, user_id):
    owner = request.user
    if request.method != 'POST':
        form = FormBlog()
    else:
        form = FormBlog(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect(reverse('blogs:personal', args=[user_id]))
    context = {'form': form, 'owner': owner}
    return render(request, 'blogs/personal_new_blog.html', context)


@login_required
def new_blog(request):

    if request.method != 'POST':
        form = FormBlog()
    else:
        form = FormBlog(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def personal_edit_blog(request, blog_id, user_id):
    blog = BlogPost.objects.get(id=blog_id)
    check_blog_owner(blog, request)
    if request.method != 'POST':
        form = FormBlog(instance=blog)
    else:
        form = FormBlog(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:personal_edit_blog', args=[user_id, blog_id]))
    context = {'form': form, 'blog_id': blog_id}
    return render(request, 'blogs/edit_blog.html', context)
