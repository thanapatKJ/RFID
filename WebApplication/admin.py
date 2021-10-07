from django.contrib import admin
from .models import ObjectInfo, NotAllowed

admin.site.register(NotAllowed)
admin.site.register(ObjectInfo)

# Register your models here.
