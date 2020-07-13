from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    tags = TaggableManager()


    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
