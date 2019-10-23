import math
import re
import secrets 
import string

from datetime import date
from django.utils.html import strip_tags
from django.utils.text import slugify


def count_words(html_string):

    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words) #joincfe.com/projects/
    return count

def get_read_time(html_string):

    count = count_words(html_string)
    read_time_min = math.ceil(count/200.0)
    return int(read_time_min)

def upload_location(instance, filename):

    N = 32
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))
    obj = str(instance._meta).split('.')
    new_id = '/'.join(map(str, obj))
    new_name = (res, filename.split(".")[1])
    _filename = '.'.join(new_name)
    new_date = date.today().strftime("%Y/%m/%d")

    return "%s/%s/%s" %(new_id, new_date, _filename)

def create_slug(instance, new_slug=None):

    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = instance.__class__.objects.filter(slug=slug).exists()
    if qs:
        new_slug = "%s-%s" %(slugify(instance.title), instance.__class__.objects.all().order_by('id').last().id)
        return create_slug(instance, new_slug=new_slug)

    return slug