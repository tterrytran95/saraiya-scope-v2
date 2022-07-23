# views responsible for receiving requests and return responses (htnl, redirect to another page, or error)
from django.http import HttpResponse
from .models import GeeksModel, Museum, CurrentFrame
from django.shortcuts import render, redirect
from .forms import MuseumForm, CurrentFrameForm
from django.views.decorators.csrf import csrf_exempt # make the upload easier

# museum view 
def museum_image_get_view(request):
    if request.method == 'GET':
        # print(request)
        img_name = request.META['QUERY_STRING'].split("=")[0]
        print(img_name)
        img_filter = Museum.objects.filter(img_name=img_name) # temp hardoding
        return render(request, 'display_museum_images.html', {'img' : img_filter})
        
@csrf_exempt # upload images without csrf        
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

def display_image(request):
    return HttpResponse("Image goes here")

def index (request):
    return HttpResponse("Hello World from Index")

# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def hello_geek (request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "hello_geek_view.html", context)


def setup_museum(request):
    return HttpResponse("Set up museum by uploading images here")