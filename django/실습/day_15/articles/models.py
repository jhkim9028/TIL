from django.db import models
# Create your models here.
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

class Articles(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(upload_to='images', blank=True, 
	                                processors=[ResizeToFill(100, 100)], format='JPEG', options={'quality':80})