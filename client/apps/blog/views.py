import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.http import HttpResponse, request, HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView


from .models import Comment, Post, Tag


class BlogView(ListView):
    
    model = Post
    paginate_by = 10 
    template_name = "base/blog.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        context['page_title'] = 'Blog'
        context['page_description'] = 'Blog'
        context['has_banner'] = True
        context['has_aside'] = False
        return context


"""
Posts
"""
class PostDetailView(DetailView):
    
    model = Post
    template_name = "base/detail/blog.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_obj = self.object
        if current_obj.seo_description is not None:
            context['page_description'] = current_obj.seo_description
        else:
            context['page_description'] = self.object.title

        print(current_obj.comments)

        context['page_title'] = current_obj.title
        context['has_banner'] = False
        context['has_aside'] = False
        return context


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','content']
    template_name_suffix = '_update_form'


@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog')


"""
Comments
"""
@method_decorator(login_required, name='dispatch')
class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('blog')


def comment_thread(request, id):
    #obj = Comment.objects.get(id=id)
    try:
        obj = Comment.objects.get(id=id)
    except:
        raise Http404

    if not obj.is_parent:
        obj = obj.parent

    content_object = obj.content_object # Post that the comment is on
    content_id = obj.content_object.id

    initial_data = {
            "content_type": obj.content_type,
            "object_id": obj.object_id
    }
    # form = CommentForm(request.POST or None, initial=initial_data)
    # if form.is_valid() and request.user.is_authenticated():
    #     c_type = form.cleaned_data.get("content_type")
    #     content_type = ContentType.objects.get(model=c_type)
    #     obj_id = form.cleaned_data.get('object_id')
    #     content_data = form.cleaned_data.get("content")
    #     parent_obj = None
    #     try:
    #         parent_id = int(request.POST.get("parent_id"))
    #     except:
    #         parent_id = None

    #     if parent_id:
    #         parent_qs = Comment.objects.filter(id=parent_id)
    #         if parent_qs.exists() and parent_qs.count() == 1:
    #             parent_obj = parent_qs.first()


    #     new_comment, created = Comment.objects.get_or_create(
    #                         user = request.user,
    #                         content_type= content_type,
    #                         object_id = obj_id,
    #                         content = content_data,
    #                         parent = parent_obj,
    #                     )
    #     return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


    context = {
        "comment": obj,
        "form": form,
    }

    return render(request, "comment_thread.html", context)

