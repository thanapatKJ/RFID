from django.contrib import admin
from .models import NotFound, ObjectHistory, ObjectInfo, NotAllowed
from django.contrib.auth.models import User

# admin.site.register(User)
admin.site.register(NotAllowed)
admin.site.register(ObjectInfo)
admin.site.register(ObjectHistory)
admin.site.register(NotFound)