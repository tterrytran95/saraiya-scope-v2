from django.contrib import admin
from .models import GeeksModel, TerrysModel, Museum, CurrentFrame

# Register your models here.
admin.site.register(Museum)
admin.site.register(CurrentFrame)
admin.site.register(GeeksModel)
admin.site.register(TerrysModel)