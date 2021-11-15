from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Post, Comment, Category
from .forms import PostForm
from django.http import HttpResponse

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return render(request, 'post/post_not_allowed.html')

    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return render(request, 'post/post_delete.html')

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')

def post_list(request):
    posts = Post.objects.all(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post/post_list.html', {'posts': posts})

def post_list_notice(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__name='공지').order_by('-published_date')
    return render(request, 'post/post_list_notice.html', {'posts': posts})

def post_list_questions(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__name='질문').order_by('-published_date')
    return render(request, 'post/post_list_questions.html', {'posts': posts})

def post_list_request(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__name='요청').order_by('-published_date')
    return render(request, 'post/post_list_request.html', {'posts': posts})

def post_list_report(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__name='제보').order_by('-published_date')
    return render(request, 'post/post_list_report.html', {'posts': posts})

def post_list_etc(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__name='기타').order_by('-published_date')
    return render(request, 'post/post_list_etc.html', {'posts': posts})

def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk)
    if request.method == "POST":
        comment = Comment()
        comment.post = post_detail
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.author = request.user
        comment.save()
    return render(request, 'post/post_detail.html', {'post': post_detail, 'comments': comments})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'post/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return render(request, 'post/post_not_allowed.html')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'post/post_edit.html', {'form': form})

def post_not_allowed(request):
    return render(request, 'post/post_not_allowed.html')


def post_list(request):
    if not request.user.is_authenticated:
        return render(request, 'post/post_must_login.html')
    else:

        page = request.GET.get('page', '1')  # 페이지

        # 조회
        question_list = Post.objects.order_by('-published_date')

        # 페이징처리
        paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)

        context = {'posts': page_obj}

        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

        search_key = request.GET.get('search_key')
        if search_key:  # 만약 검색어가 존재하면
            posts = posts.filter(title__icontains=search_key)  # 제목에 해당 검색어를 포함한 queryset 가져오기
            return render(request, 'post/post_list.html', {'posts': posts})

        return render(request, 'post/post_list.html', context)

def post_confirm_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return render(request, 'post/post_not_allowed.html')

    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        return render(request, 'post/post_confirm_delete.html')

    elif request.method == 'GET':
        post = Post.objects.get(pk=pk)
        return render(request, 'post/post_confirm_delete.html')

# 댓글 삭제
def comment_delete(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user != comment.author:
        return render(request, 'post/post_not_allowed.html')

    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return render(request, 'post/comment_delete.html')

    elif request.method == 'GET':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return render(request, 'post/comment_delete.html')

