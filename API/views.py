from django.shortcuts import render
from WebApplication.models import ObjectInfo, NotAllowed
from django.http import JsonResponse

def getAllItem(request):
    objects = ObjectInfo.objects.all()
    return JsonResponse({"objects":list(objects.values())})

def getAllNotAllowed(request):
    objects = NotAllowed.objects.all()
    return JsonResponse({"objects":list(objects.values())})
