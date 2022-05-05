from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ObjectInfo(models.Model):
    all_status = [
        ('อุปกรณ์อยู่','อุปกรณ์อยู่'), 
        ('อุปกรณ์ไม่อยู่','อุปกรณ์ไม่อยู่'), 
        ('กำลังดำเนินการ','กำลังดำเนินการ'),
        ('ถูกยืม','ถูกยืม'),
        ('คืนของ','คืนของ'),
    ]
    tag_id = models.CharField(max_length=200, primary_key=True)
    tag_name = models.CharField(max_length=50)
    add_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        default='อุปกรณ์อยู่',
        choices=all_status
    )
    picture = models.ImageField(upload_to="ObjectInfo",null=True,blank=True)

    def __str__(self):
        return self.tag_name +'-'+ self.status

class NotAllowed(models.Model):
    picture = models.ImageField(upload_to="NotAllowed")
    date_time = models.DateTimeField()

    def __str__(self):
        return str(self.date_time)

class NotFound(models.Model):
    tag = models.ForeignKey(ObjectInfo,on_delete=models.CASCADE)
    not_allow = models.ForeignKey(NotAllowed, on_delete=models.CASCADE)
    takeout_time = models.DateTimeField(default=datetime.now())

class ObjectHistory(models.Model):
    tag_id = models.ForeignKey(ObjectInfo, on_delete=models.CASCADE)
    student_id = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    picture = models.ImageField(null=True, blank=True,upload_to="ObjectHistory")
    borrow_time = models.DateTimeField(null=True,blank=True)
    return_time = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return str(self.tag_id.tag_name) + " - "+ self.student_id