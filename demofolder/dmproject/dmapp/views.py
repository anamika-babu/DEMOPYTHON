from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"demo.html")
def values(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    value=x+y
    value1=x-y
    value2=x*y
    value3=x/y
    return render(request,"result.html",{'result':value,'result1':value1,'result2':value2,'result3':value3})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("contact number is 6236854710")
# def details(request):
#     return render(request,"details.html")
# def thanks(request):
#     return HttpResponse("thanks to visting")