from django.http import HttpResponse
from django.template.loader import render_to_string


def index(_):
    file_content = render_to_string("blog_site/home.html")
    return HttpResponse(file_content)



