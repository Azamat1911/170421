from django.db import models

# Create your models here.
class Post(models.Model):
    name  = models.CharField(max_length=300)
    content = models.TextField()
    cover = models.FileField(null=True,blank=True)
    dateofcreation = models.DateTimeField(auto_now=True)
    viewscounter = models.IntegerField(default=0)
