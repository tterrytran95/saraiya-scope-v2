# views responsible for receiving requests and return responses (htnl, redirect to another page, or error)
from django.http import HttpResponse
from .models import Museum, CurrentFrame
from django.shortcuts import render, redirect
from .forms import MuseumForm, CurrentFrameForm
from django.views.decorators.csrf import csrf_exempt # make the upload easier

# museum view # tt
def museum_image_get_view(request):
    if request.method == 'GET':
        # print('request: ', request.META)
        img_name = request.META['QUERY_STRING'].split("=")[1]
        img_filter = CurrentFrame.objects.filter(img_name=img_name.split(".")[0]) # temp hardoding
        return render(request, 'display_museum_images.html', {'img' : img_filter})
        
@csrf_exempt # upload images without csrf # tt
def post_cur_image(request):
    if request.method == 'POST':
        print(request)
        print("POST")
        print(request.POST)
        print("FILES")
        print(request.FILES)
        form = CurrentFrameForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            # print("### form")
            # print(form)
            return redirect('error')
    else:
        form = CurrentFrameForm()
    return render(request, 'museum_upload.html', {'form' : form})
        
# DEPRECATED
        
@csrf_exempt # upload images without csrf
def museum_image_upload_view(request):
    print(request)
    if request.method == 'POST':
        form = MuseumForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MuseumForm()
        
    return render(request, 'museum_upload.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')

def error(request):
    return HttpResponse('error with upload')