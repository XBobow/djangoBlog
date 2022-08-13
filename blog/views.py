from django.shortcuts import render, get_object_or_404
from django.db.models import Q, F
from django.core.paginator import Paginator
from .models import Category, Post


# Create your views here.

def index(request):
    # 首页
    post_list = Post.objects.all()
    # 分页
    paginator = Paginator(post_list, 5)  # 第二个参数2代表每页显示几个
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'blog/index.html', context)


def category_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.post_set.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'category': category, 'page_obj': page_obj}
    return render(request, 'blog/list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    prev_post = Post.objects.filter(add_date__lt=post.add_date).last()
    next_post = Post.objects.filter(add_date__gt=post.add_date).first()

    context = {'post': post, 'prev_post': prev_post, 'next_post': next_post}
    return render(request, 'blog/detail.html', context)


# 搜索
def search(request):
    keyword = request.GET.get('keyword')
    if not keyword:
        post_list = Post.objects.all()
    else:
        post_list = Post.objects.filter(
            Q(title__icontains=keyword) | Q(desc__icontains=keyword) | Q(content__icontains=keyword))
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'blog/index.html', context)


def archives(request, year, month):
    post_list = Post.objects.filter(add_date__year=year, add_date__month=month)
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'year': year, 'month': month}
    return render(request, 'blog/archives_list.html', context)
