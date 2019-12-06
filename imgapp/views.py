from django.shortcuts import render
from .models import Img
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def uploadImg(request):   # upload images
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
    imgs = Img.objects.all() # get images (directory) from databases
    context = {
        'imgs' : imgs
    }
    return render(request, 'showImg.html', context)