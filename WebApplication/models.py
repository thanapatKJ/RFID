from django.db import models
from django.contrib.auth.models import User

class ObjectInfo(models.Model):
    all_status = [
        ('อยู่','อุปกรณ์อยู่'),
        ('ไม่อยู่','อุปกรณ์ไม่อยู่'),
    ]
    tag_id = models.CharField(max_length=200, primary_key=True)
    tag_name = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        default='ไม่อยู่',
        choices=all_status
    )
    borrow_time = models.DateTimeField(null=True,blank=True)
    student_id = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    picture = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.tag_name +'-'+ self.status

class NotAllowed(models.Model):
    picture = models.ImageField()
    date_time = models.DateTimeField()
    def __str__(self):
        return str(self.date_time)

        