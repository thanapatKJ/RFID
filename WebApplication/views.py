from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from datetime import datetime

from django.contrib import messages

from .forms import UserForm, ObjectForm
from .models import NotFound, ObjectHistory, ObjectInfo, NotAllowed

from django.core.mail import send_mail
from RFID.settings import EMAIL_HOST_USER

def login(request):
    error = ""
    if request.user.is_authenticated:
        return redirect('/')

    elif request.method == 'POST':
        user = authenticate(request ,
            username=request.POST['username'],
            password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            error = "User หรือ Password ไม่ถูกต้อง"
    return render(request,'WebApplication/login.html',{
        'error':error,
    })

def logout(request):
    auth_logout(request)
    return redirect('/')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method== 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                print("invalid")
        else:
            form = UserForm()
    form = UserForm(request.POST)
    return render(request,'WebApplication/register.html',{'form':form})

def home(request):
    # objects = []
    # subject="การยืมครุภัณฑ์โดยไม่ได้รับอนุญาต"
    # message="ชื่ออุปกรณ์: Hammer \nชื่อผู้ยืม: ธนพัฒน์ คล้ายจำแลง \nวันเวลา:12/10/2564 1:32"
    # recipient="thanapatkjm@gmail.com"
    # send_mail(subject,message,EMAIL_HOST_USER,[recipient],fail_silently=False)
    return render(request,'WebApplication/home.html',)

def edit(request,tag_id):
    objects = ObjectInfo.objects.get(tag_id=tag_id)
    if request.method== 'POST':
        if(request.POST['status'] != objects.status):
            if(request.POST['status']=="กำลังดำเนินการ"):
                thistag=ObjectInfo.objects.get(tag_id=tag_id)
                ObjectHistory.objects.create(
                    tag_id=thistag,
                    student_id=request.POST['student_id'],
                )
            elif (objects.status == 'กำลังดำเนินการ' and (request.POST['status']=='อุปกรณ์ไม่อยู่' or request.POST['status']=='อุปกรณ์อยู่')):
                ObjectHistory.objects.filter(tag_id=tag_id).latest('id').delete()
            elif (objects.status == 'ถูกยืม' and request.POST['status']=='คืนของ'):
                latest = ObjectHistory.objects.filter(tag_id=tag_id).latest('id')
                latest.return_time = datetime.now()
                latest.save()
            objects.tag_name=request.POST['tag_name']
            objects.status=request.POST['status']
            objects.save()
            return redirect('/')
    return render(request, 'WebApplication/edit.html',{'objects':objects})

def delete_history(request,id):
    object = ObjectHistory.objects.get(id=id)
    tag_id = object.tag_id.tag_id
    object.delete()
    return redirect('WebApplication:item',tag_id=tag_id)

def delete(request,tag_id):
    ObjectInfo.objects.get(tag_id=tag_id).delete()
    return redirect('/')

def add(request):
    if request.method == 'POST':
        form = ObjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ObjectForm()
    return render(request, 'WebApplication/add.html',{'form':form})

def item(request,tag_id):
    objects = ObjectInfo.objects.get(tag_id=tag_id)
    objects_history = ObjectHistory.objects.filter(tag_id=tag_id)
    return render(request, 'WebApplication/item.html',{
        'objects':objects,
        'objects_history':objects_history})

def not_allow(request):
    objects = NotAllowed.objects.all()
    return render(request, 'WebApplication/not_allow.html',{'objects':objects})

def delete_nl(request,id):
    NotAllowed.objects.get(id=id).delete()
    return redirect('WebApplication:not_allow')

def editNotAllow(request,id):
    objects = NotAllowed.objects.get(id=id)
    return render(request, 'WebApplication/item_notAllow.html',{'objects':objects})

def notFound(request):
    return render(request, 'WebApplication/not_found.html')

def deleteNF(request,id):
    NotFound.objects.get(id=id).delete()
    return redirect(request, 'WebApplication:notFound')
