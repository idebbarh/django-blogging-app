from django.db import models


class Blog(models.Model) :
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    date = models.DateField()
    image = models.CharField(max_length=255)
    slug = models.SlugField()

    objects = models.Manager()
