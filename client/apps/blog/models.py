from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


from ckeditor.fields import RichTextField

# Get Read Time further implementation
from client.apps.utils.base import get_read_time, upload_location, create_slug


class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id= obj_id).filter(parent=None)
        return qs


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


class Tag(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE,verbose_name=_('Autor'))
    title = models.CharField(max_length=144, blank=True)
    slug = models.SlugField(unique=True, blank=True,verbose_name=_('Nombre url SEO'))
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='+', on_delete=models.CASCADE,verbose_name=_('Actualizado por'), blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name=_('Fecha de creación'))

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True)
    object_id = models.PositiveIntegerField(blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    content = RichTextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("comments-thread", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("comment-delete", kwargs={"id": self.id})
        
    def children(self): #replies
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        default=1
    )
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=120, blank=True)
    seo_description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField(blank=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(
        auto_now=True, 
        auto_now_add=False, 
        blank=True
    )
    read_time =  models.IntegerField(default=0, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    tag = models.ManyToManyField(
        Tag, 
        blank=True,
        verbose_name=_('Tag asociado')
    )
    image = models.ImageField(
        upload_to=upload_location, 
        null=True, 
        blank=True, 
        width_field="width_field", 
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0, blank=True)
    width_field = models.IntegerField(default=0, blank=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]


    def get_markdown(self):
        content = self.content
        markdown_text = content
        return mark_safe(markdown_text)

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    
    if not instance.slug:
        instance.slug = create_slug(instance)
    
    if instance.content:
        html_string = instance.get_markdown()
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var

def pre_save_tag_receiver(sender, instance, *args, **kwargs):
    
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
pre_save.connect(pre_save_tag_receiver, sender=Tag)