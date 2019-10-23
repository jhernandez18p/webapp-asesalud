from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .views import BlogView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, \
    CommentDeleteView, comment_thread


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail'),

    # path('post/nuevo', RedirectView.as_view(url='/blog/'), name='post-create'),
    path('post/nuevo', RedirectView.as_view(url='/blog/'), name='post-create'),
    
    # path('post/<slug:slug>/edit', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/edit', RedirectView.as_view(url='/blog/'), name='post-update'),
    
    # path('post/<slug:slug>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/delete', RedirectView.as_view(url='/blog/'), name='post-delete'),

    # path('comentario/nuevo', comment_thread, name='comment-create'),
    path('comentario/nuevo', RedirectView.as_view(url='/blog/'), name='comment-create'),
    
    path('comentario/<int:id>', comment_thread, name='comments-thread'),
    
    # path('comentario/<int:id>/delete', CommentDeleteView.as_view(), name='comment-delete'),
    path('comentario/<int:id>/delete', RedirectView.as_view(url='/blog/'), name='comment-delete'),
]