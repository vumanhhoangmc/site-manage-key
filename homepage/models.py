from django.db import models
from django.utils import timezone, dateformat
from datetime import date
# Create your models here.
class Managekey(models.Model):
    key = models.CharField(max_length=100, default='hoangdzsvipprovip chua nhap key')
    owner = models.CharField(max_length=200, default='hoangdzsvip')
    tool = models.CharField(max_length=200, default='tool')
    date_create = models.CharField(default=dateformat.format(timezone.datetime.now(), 'Y-m-d'), max_length=100)
    expiration_date = models.CharField(default=dateformat.format(timezone.datetime.now(), 'Y-m-d'), max_length=100)
    hsd = models.IntegerField(default=30)

    def __str__(self):
        return self.key 