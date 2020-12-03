from django.db import models
from django.contrib.auth.models import User
# Create your models


class BlogPost(models.Model):

    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ImportFile(models.Model):
    file = models.FileField(upload_to='File')
    name = models.CharField(max_length=50, verbose_name='文件名')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
