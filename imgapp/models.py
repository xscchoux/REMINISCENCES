from django.db import models

# Create your models here.
class Img(models.Model):
    img_url = models.ImageField(upload_to='img') # upload_to指定圖片上傳的途徑，如果不存在則自動創建