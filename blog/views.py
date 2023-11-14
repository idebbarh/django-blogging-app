import os
import random
from django.http import HttpResponse,Http404
from django.template.loader import render_to_string
from blog.models import Blog
from blog_site.settings import BASE_DIR

images_dir = BASE_DIR / "static/assets/images/"
images_paths = [image for image in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir,image))]

def index(_):
    random_image_index = random.randrange(0,len(images_paths)-1)
    random_landing_image = images_paths[random_image_index]
    latest_blogs_data = Blog.objects.order_by("date")[0:5]
    file_content = render_to_string("blog/index.html",{"landing_image":random_landing_image,"latest_blogs":latest_blogs_data})

    return HttpResponse(file_content)

def blogs(_):
    blogs_data = Blog.objects.all()
    file_content = render_to_string("blog/blogs.html",{"all_blogs":blogs_data}) 

    return HttpResponse(file_content)

def blog(_,slug):
    try :
        blog_data = Blog.objects.get(slug=slug)
        random_image_index = random.randrange(0,len(images_paths)-1)
        random_landing_image = images_paths[random_image_index]
        file_content = render_to_string("blog/blog.html",{"landing_image":random_landing_image,"single_blog":blog_data})

        return HttpResponse(file_content)

    except Blog.DoesNotExist :
        raise Http404()

