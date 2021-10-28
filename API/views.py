from WebApplication.models import ObjectInfo, NotAllowed
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User

from rest_framework import generics

import json

from django.core.mail import send_mail
from RFID.settings import EMAIL_HOST_USER

def getAllItem(request):
    objects = ObjectInfo.objects.all()
    return JsonResponse({"objects":list(objects.values())})


def getAllNotAllowed(request):
    objects = NotAllowed.objects.all()
    return JsonResponse({"objects":list(objects.values())})


class tagData(generics.GenericAPIView):
    # ส่ง tag_id พร้อม status ของทุกสถานะยกเว้นสถานะถูกยืม
    def get(self, request):
        objects = []
        for list in ObjectInfo.objects.exclude(status='ถูกยืม'):
            objects.append({
                'tag_id':list.tag_id,
                'status':list.status})
        return HttpResponse(json.dumps(objects), content_type='application/json')
    
    # รับ tag_id และ status กลับมา save ไว้ใน database
    def post(self, request):
        # objects = []
        # for list in ObjectInfo.objects.all():
        #     objects.append({'tag_id':list.tag_id})
        # return HttpResponse(json.dumps(objects), content_type='application/json')
        objects = ObjectInfo.objects.get(tag_id=request.POST['tag_id'])
        objects.status = 'ถูกยืม'
        objects.save()

class notAllowed(generics.GenericAPIView):
    # ส่งทุก notAllowed # ไม่ได้ใช้
    def get(self, request):
        objects = []
        for list in NotAllowed.objects.all():
            objects.append({'date_time':list.date_time})
        print(objects)
        return HttpResponse(json.dumps(objects), content_type='application/json')

    # รับ NotAllowed กลับมาเก็บไว้ใน Database พร้อมส่ง Email ไปให้ superuser
    def post(self,request):
        
        # subject="การยืมครุภัณฑ์โดยไม่ได้รับอนุญาต"
        # message="วันเวลา:"+request.POST['date_time']
        # recipient=User.objects.get(username='admin').email
        # send_mail(subject,message,EMAIL_HOST_USER,[recipient],fail_silently=False)
        objects = {'status':'success'}
        return HttpResponse(json.dumps(objects), content_type='application/json')