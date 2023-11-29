from django.db import models

# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysql_test/mysql_test.settings')
# django.setup()

# Create your models here.





# 在终端进行更改数据内容：python manage.py shell
# 进入python终端编辑，from mysql_te.models import test1
# 其中mysql_te是app名，test1是需要进行更改的库名
class test1(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)

class sale_M(models.Model):
    shopname = models.CharField(max_length=10, blank=False)
    call = models.CharField(max_length=20)
    cashier = models.CharField(max_length=10)
    saletime = models.DateField()

class sale_Date(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=100, blank=False)
    number = models.DateField()
    Mlink=models.ForeignKey("sale_M",on_delete=models.CASCADE)

