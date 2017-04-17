from django.db import models
 
# Create your models here.
class Post(models.Model):
    short_id = models.SlugField(max_length=6,primary_key=True)
    httpurl = models.URLField(max_length=500)
    text = models.TextField()
def __str__(self):
    return self.title
