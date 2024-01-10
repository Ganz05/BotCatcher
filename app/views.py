from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.


def create_student(request):
    ELSO=studentForm()
    d={"ELSO":ELSO}
    if request.method=='POST':
        CLSO=studentForm(request.POST)
        if CLSO.is_valid():
            id=CLSO.cleaned_data['sid']
            na=CLSO.cleaned_data['sname']
            db=CLSO.cleaned_data['DOB']
            em=CLSO.cleaned_data['email']
            re=CLSO.cleaned_data['re_enter']

            NSO=student.objects.get_or_create(sid=id,sname=na,DOB=db,email=em,re_enter=re)[0]
            NSO.save()

            return HttpResponse('Data Inserted Succussfully')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'create_student.html',d)