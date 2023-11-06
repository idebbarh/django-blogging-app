from django.http import HttpResponse
from django.template.loader import render_to_string


def blogs(_):
    file_content = render_to_string("blog/blogs.html") 
    return HttpResponse(file_content)
