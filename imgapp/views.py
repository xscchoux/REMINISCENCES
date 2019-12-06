from django.shortcuts import render
from .models import Img
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def uploadImg(request):   # 圖片上傳函數
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
        imgs = Img.objects.all()
        context = {
            'imgs' : imgs
        }
        return render(request, 'showImg.html',context)
    return render(request, 'imgupload.html')

def showImg(request):
    imgs = Img.objects.all() # 从数据库中取出所有的图片路径
    context = {
        'imgs' : imgs
    }
    return render(request, 'showImg.html', context)