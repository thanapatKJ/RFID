from WebApplication.models import NotFound, ObjectInfo, NotAllowed,ObjectHistory
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
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
        objects = ObjectInfo.objects.get(tag_id=request.POST['tag_id'])
        if objects.status == 'กำลังดำเนินการ' and request.POST['status']=="ถูกยืม":
            history = ObjectHistory.objects.filter(
                    tag_id=objects,
                ).latest('id')
            history.borrow_time = datetime.now()
            history.picture = request.FILES['picture']
            history.save()
            objects.status = 'ถูกยืม'
            objects.save()

            subject="การยืมครุภัณฑ์"
            recipient=User.objects.get(username='admin').email
            message="ชื่ออุปกรณ์: "+str(history.tag_id.tag_name)+" \nรหัสนักศึกษา: "+str(history.student_id) + " \nวันเวลา:" +str(history.borrow_time)
            send_mail(subject,message,EMAIL_HOST_USER,[recipient],fail_silently=False)
        elif request.POST['status'] == 'อุปกรณ์ไม่อยู่' or request.POST['status'] == 'อุปกรณ์อยู่':
            objects.status = request.POST['status']
            objects.save()
        elif objects.status == 'คืนของ' and request.POST['status']=="อุปกรณ์อยู่":
            history = ObjectHistory.objects.filter(
                    tag_id=objects,
                ).latest('id')
            history.return_time = datetime.now()
            history.save()
            objects.status = 'อุปกรณ์อยู่'
            objects.save()

class notAllowed(generics.GenericAPIView):
    # รับ NotAllowed กลับมาเก็บไว้ใน Database พร้อมส่ง Email ไปให้ superuser
    def post(self,request):
        NotAllowed.objects.create(
            picture=request.FILES['picture'],
            date_time=datetime.now())
        subject="การยืมครุภัณฑ์โดยไม่ได้รับอนุญาต"
        message="วันเวลา:"+str(datetime.now())
        recipient=User.objects.get(username='admin').email
        print(recipient)
        send_mail(subject,message,EMAIL_HOST_USER,[recipient],fail_silently=False)
        objects = {'status':'success'}
        return HttpResponse(json.dumps(objects), content_type='application/json')

class notFound(generics.GenericAPIView):
    
    def post(self,request):
        print('not Found ------')
        not_allow = NotAllowed.objects.latest('id')
        print(not_allow)
        tag = ObjectInfo.objects.get(tag_id=request.POST['tag_id'])
        print(tag)
        NotFound.objects.create(tag=tag,not_allow=not_allow,takeout_time=datetime.now())
