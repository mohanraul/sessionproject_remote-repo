from django.shortcuts import render
from . import forms

# Create your views here.
def nameview(request):
    form=forms.nameform()
    return render(request,"testapp/name.html",{'form':form})

def salview(request):
    name=request.GET['name']
    request.session['name'] = name
    form = forms.salform()
    return render(request,"testapp/sal.html",{'form':form})

def qualview(request):
    salary=request.GET['salary']
    request.session['salary'] = salary
    form =forms.Qualificationform()
    return render(request,"testapp/qual.html",{"form":form})

def resview(request):
    qualification=request.GET['qualification']
    request.session['qualification'] = qualification
    return render(request,"testapp/res.html")
