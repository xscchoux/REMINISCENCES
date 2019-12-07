from django.db import models

# Create your models here.
class Img(models.Model):
    name = models.CharField(max_length=200) 
    img_url = models.ImageField(upload_to='img') # upload the image to the folder 'img'