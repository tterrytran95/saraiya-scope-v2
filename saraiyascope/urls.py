from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .consumers import MuseumConsumer

#now import the views.py file into this code
from . import views # import the view for each url
urlpatterns=[
  path('route/MUSEUM/', MuseumConsumer.as_asgi()),
  path('admin/', admin.site.urls),
  path('museum_image', views.museum_image_get_view, name = 'museum_image'),
  path('post_cur_image', views.post_cur_image, name = 'post_cur_image'), 
  
  path('success', views.success, name = 'success'),
  path('error', views.error, name = 'error'),
  path('image_upload', views.museum_image_upload_view, name = 'image_upload'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)