from django.db import models

# Create your models here.
class VideoFile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    Video_file = models.FileField(upload_to='../media', null=True)

    def __str__(self):
        return self.title