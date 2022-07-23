from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#now import the views.py file into this code
from . import views # import the view for each url

urlpatterns=[
  path('',views.index),
  path('admin/', admin.site.urls),
  path('museum/', views.display_image),
  path('setup/', views.setup_museum),
  path('image_upload', views.museum_image_upload_view, name = 'image_upload'),
  path('post_cur_image', views.post_cur_image, name = 'post_cur_image'),
  path('success', views.success, name = 'success'),
  path('error', views.error, name = 'error'),
  path('museum_image', views.museum_image_get_view, name = 'museum_image'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)