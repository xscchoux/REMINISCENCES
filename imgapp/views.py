from django.shortcuts import render, redirect 
# from .models import Img
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse
# Create your views here.

@login_required
def uploadImg(request):   # upload images
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImgForm()
    return render(request, 'imgupload.html',{'form':form})

def success(request): 
    return HttpResponse('successfuly uploaded') 

def showImg(request):
    if request.method == 'GET':
        imgs = Img.objects.all() # get the URLs of all images in the database
        context = {'images' : imgs}
    return render(request, 'showImg.html', context)


# from django.shortcuts import render
# from .models import Img
# from django.contrib.auth.decorators import login_required
# # Create your views here.

# @login_required
# def uploadImg(request):   # upload images
#     if request.method == 'POST':
#         img = Img(img_url=request.FILES.get('img'))
#         img.save()
#         imgs = Img.objects.all()
#         context = {
#             'imgs' : imgs
#         }
#         return render(request, 'showImg.html',context)
#     return render(request, 'imgupload.html')

# def showImg(request):
#     imgs = Img.objects.all() # get images (directory) from databases
#     context = {
#         'imgs' : imgs
#     }
#     return render(request, 'showImg.html', context)