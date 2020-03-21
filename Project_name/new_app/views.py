from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun(request):
    return render(request,'Home.html',{'Name':'Santosh'})
    #return HttpResponse('<h1>Hello, World!</h1>')
def update(request):
    n1 = int(request.GET['num1'])
    n2 = int(request.GET['num2'])
    res = n1 + n2   
    return render(request,'result.html',{'n_result':res})

def naming(request):
    name = request.GET['na_me']
    return render(request, 'Home.html',{'namedd':name})