from django.urls import path
from post.views import post_list, post_detail, post_edit, post_delete, post_new, post_not_allowed, post_confirm_delete, comment_delete, post_list_notice, post_list_questions, post_list_request, post_list_report, post_list_etc

app_name = 'post'

urlpatterns = [
    path('post_list', post_list, name='post_list'),

    path('post_list_notice', post_list_notice, name='post_list_notice'),
    path('post_list_questions', post_list_questions, name='post_list_questions'),
    path('post_list_request', post_list_request, name='post_list_request'),
    path('post_list_report', post_list_report, name='post_list_report'),
    path('post_list_etc', post_list_etc, name='post_list_etc'),

    path('post/<pk>/', post_detail, name='post_detail'),
    path('new/', post_new, name='post_new'),
    path('post/<pk>/edit/', post_edit, name='post_edit'),
    # path('post/<pk>/delete/', post_delete, name='post_delete'),
    path('post_not_allowed', post_not_allowed, name='post_not_allowed'),

    path('post/<pk>/confirm_delete/', post_confirm_delete, name='post_confirm_delete'),
    path('post/<pk>/confirm_delete/delete/', post_delete, name='post_delete'),
    # 댓글 삭제
    path('post/<post_pk>/comment_delete/<comment_pk>', comment_delete, name='comment_delete'),
]