import os
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from blog_site.settings import BASE_DIR

images_dir = BASE_DIR / "static/assets/images/"

images_paths = [image for image in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir,image))]

def index(_):
    random_image_index = random.randrange(0,len(images_paths)-1)
    file_content = render_to_string("blog_site/home.html",{"landing_image":images_paths[random_image_index]})
    return HttpResponse(file_content)



