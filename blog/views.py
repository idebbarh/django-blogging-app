from datetime import datetime 
import os
import random
from django.http import HttpResponse,Http404
from django.template.loader import render_to_string
from blog_site.settings import BASE_DIR

images_dir = BASE_DIR / "static/assets/images/"
images_paths = [image for image in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir,image))]


blogs_info = [
{
    "title":"this is a title",
    "description":"lorem bla bla bla bla bla bla bla",
    "content":"""Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eius sequi totam
      reiciendis vel! Officia unde quo alias sed, dolore aperiam, obcaecati
      atque tenetur, expedita nostrum cum eaque esse ipsam sapiente?
    """,
    "date":datetime.now().strftime("%d %b %Y"),
    "image":"alberto-restifo-cFplR9ZGnAk-unsplash.jpg",
    "slug":'this-is-blog-number-1'
},
{
    "title":"this is a title",
    "description":"lorem bla bla bla bla bla bla bla",
    "content":"""Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eius sequi totam
      reiciendis vel! Officia unde quo alias sed, dolore aperiam, obcaecati
      atque tenetur, expedita nostrum cum eaque esse ipsam sapiente?
    """,
    "date":datetime.now().strftime("%d %b %Y"),
    "image":"marita-kavelashvili-ugnrXk1129g-unsplash.jpg",
    "slug":'this-is-blog-number-2'
},
{
    "title":"this is a title",
    "description":"lorem bla bla bla bla bla bla bla",
    "content":"""Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eius sequi totam
      reiciendis vel! Officia unde quo alias sed, dolore aperiam, obcaecati
      atque tenetur, expedita nostrum cum eaque esse ipsam sapiente?
    """,
    "date":datetime.now().strftime("%d %b %Y"),
    "image":"irina-iriser-2Y4dE8sdhlc-unsplash.jpg",
    "slug":'this-is-blog-number-3'
}
]


def index(_):
    random_image_index = random.randrange(0,len(images_paths)-1)
    random_landing_image = images_paths[random_image_index]

    file_content = render_to_string("blog/index.html",{"landing_image":random_landing_image,"latest_blogs":blogs_info})
    return HttpResponse(file_content)

def blogs(_):
    file_content = render_to_string("blog/blogs.html",{"all_blogs":blogs_info}) 
    return HttpResponse(file_content)

def blog(_,slug):
    blog_info = [blog_info for blog_info in blogs_info if blog_info['slug'] == slug]

    if not blog_info :
        raise Http404()

    random_image_index = random.randrange(0,len(images_paths)-1)
    random_landing_image = images_paths[random_image_index]

    file_content = render_to_string("blog/blog.html",{"landing_image":random_landing_image,"single_blog":blog_info[0]})
    return HttpResponse(file_content)
