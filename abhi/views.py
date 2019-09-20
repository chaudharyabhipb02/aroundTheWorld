from django.shortcuts import render
from django.http import HttpResponse
import datetime
today=datetime.datetime.now()

def hello(request):
    text="<h2>welcome to django</h2>"
    return HttpResponse(text)
def template_home(request):
    return render(request,"abhi/base.html")
# Create your views here.
def order_demo(request):
    item_list=["pen","pencil","notebook"]
    uname= "ABHI"
    return render(request,"abhi/order.html",{"person_name":uname,"ship_date":today,"item_list":item_list})
def index(request):
    return render(request,"abhi1/index.html")