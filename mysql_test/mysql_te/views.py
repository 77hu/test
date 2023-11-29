from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from mysql_te import models


# Create your views here
def te_test1(request):
    student_queryset = models.test1.objects.all()
    return render(request,"student.html",{"student_queryset": student_queryset})


def date_view(request, date):
    # date = datetime(int(year), int(month), int(day))
    # date = datetime.strptime(date, "%Y_%m_%d")
    return HttpResponse("Date: " + str(date)+"新闻直播间")