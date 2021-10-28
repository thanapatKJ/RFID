from django.contrib import admin
from .models import ObjectHistory, ObjectInfo, NotAllowed

admin.site.register(NotAllowed)
admin.site.register(ObjectInfo)
admin.site.register(ObjectHistory)