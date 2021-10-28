from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ObjectInfo(models.Model):
    all_status = [
        ('อุปกรณ์อยู่','อุปกรณ์อยู่'), 
        ('อุปกรณ์ไม่อยู่','อุปกรณ์ไม่อยู่'), 
        ('กำลังดำเนินการ','กำลังดำเนินการ'),
        ('ถูกยืม','ถูกยืม'),
    ]
    tag_id = models.CharField(max_length=200, primary_key=True)
    tag_name = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        default='อยู่',
        choices=all_status
    )
    def __str__(self):
        return self.tag_name +'-'+ self.status

class NotAllowed(models.Model):
    picture = models.ImageField()
    date_time = models.DateTimeField()
    def __str__(self):
        return str(self.date_time)

class ObjectHistory(models.Model):
    tag_id = models.ForeignKey(ObjectInfo, on_delete=models.CASCADE)
    student_id = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    picture = models.ImageField(null=True, blank=True)
    borrow_time = models.DateTimeField()
    return_time = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return str(self.tag_id.tag_name) + " - "+ self.student_id

    # @classmethod
    # def borrow(cls):
    #     cls.tag_id.status = "กำลังดำเนินการ"
    #     cls.borrow_time = datetime.now()
    #     return cls

    # @classmethod
    # def ret(cls):
    #     cls.tag_id.status = "อุปกรณ์อยู่"
    #     cls.return_time = datetime.now()
    #     return cls