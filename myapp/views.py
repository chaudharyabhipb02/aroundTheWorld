from django.shortcuts import render
from .form import RegistrationForm1
from .form import LoginForm1
from .form import feedbackform
from .models import tb_register
from .models import feedback

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

def pro(request):
    return render(request,"myapp/index.html")
def about(request):
    return render(request,"myapp/about.html")

def contact(request):
    return render(request,"myapp/contacts.html")
def destination(request):
    return render(request,"myapp/destinations.html")
def tour(request):
    return render(request,"myapp/tours.html")

def home(request):
    return render(request,'myapp/home.html')

def register(request):
    if request.method=='POST':

        form = RegistrationForm1(request.POST)
        if form.is_valid():
            name1=form.cleaned_data["name"]
            email1=form.cleaned_data["email"]
            contact1 = form.cleaned_data["contact"]
            address1 = form.cleaned_data["address"]
            password1 = form.cleaned_data["password"]
            gender1 = form.cleaned_data["gender"]
            p=tb_register(name = name1,email=email1,contact=contact1,address=address1,password=password1,gender=gender1)
            p.save()
            return HttpResponseRedirect('myapp/login')

        else:
            return render(request, "myapp/form.html", {'form':form})
    else:
         form =RegistrationForm1()
         return render(request, "myapp/form.html", {'form':form})

def login(request):
    if request.session.has_key("username"):
        username=request.session["username"]
        return render(request, "myapp/login.html", {'msg': "You are already Logged In as "+username, 'btn_chk':False})
    else:
        if request.method == 'POST':
            form = LoginForm1(request.POST)
            if form.is_valid():
                u_email=form.cleaned_data["email"]
                u_password = form.cleaned_data["password"]
                p=tb_register.objects.filter(email=u_email,password=u_password)
                if(p.count()>0):
                    request.session['username']=u_email
                    return render(request,"myapp/login.html",{'msg':"You are Successfully Logged In",'btn_chk':False})
                else:
                    print('try again',p)
                    return HttpResponseNotFound('<h1>no page here</h1>')
            else:
                print("\n\n this is else block:{0}\n\n")
                return render(request,"myapp/login.html",{'form':form,'btn_chk':True})
        else:
            form=LoginForm1()
            print("\n\n tis is else block:{0}\n\n")
            return render(request,"myapp/login.html",{"form":form,'btn_chk':True})


def contacts(request):
    username=""
    if request.session.has_key("username"):
        username=request.session["username"]
        if request.method == 'POST':
                form = feedbackform(request.POST,request.FILES)
                if form.is_valid():
                    name1 = form.cleaned_data["name"]
                    message1 = form.cleaned_data["message"]
                    image1 = form.cleaned_data["image"]
                    s1 = tb_register.objects.get(email = username)
                    s = feedback(name=name1, message=message1,uid = s1, image=image1)
                    s.save()
                    print("submitted")
                    form = feedbackform()
                    return render(request, "myapp/contacts.html", {'form': form,'msg':"Thanks for Sharing Feedback",'btn_chk':True})
                else:
                    print("else",".....")
                    return render(request,"myapp/contacts.html",{'form':form,'btn_chk':True})
        else:
                form=feedbackform()
                return render(request,"myapp/contacts.html",{"form":form})
    else:
        return render(request, "myapp/contacts.html", {'msg':"For SignUp","click":"Click Here",'btn_chk':False})
def display_feedback(request):
    p=feedback.objects.all()
    print(p)
    return render(request,"myapp/about.html",{"key":p})



def delete_session(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return HttpResponseRedirect("home")
def common(request):
    return render(request,'myapp/com.html')
def amritsar(request):
    return render(request,'myapp/amritsar.html')

from .form import flight_booking
from .models import flight_avail

def book(request):
    s1=flight_avail.objects.all()
    s2=list(s1)
    return render(request,'myapp/viewflites.html',{'s2':s2})


from .form import flight_search

def search(request):
     if request.method == 'POST':
          form = flight_search(request.POST)
          if form.is_valid():
                From = form.cleaned_data["From"]
                to = form.cleaned_data["to"]
                date = form.cleaned_data["date"]
                category = form.cleaned_data["category"]
                trip_type = form.cleaned_data["trip_type"]

                s=flight_avail.objects.filter(From=From,to=to,date=date,category=category,trip_type=trip_type)
                if (s.count() > 0):



                    #s1=flight_avail.objects.get(From=From,to=to,date=date)
                    s2=list(s)
                    return render(request,'myapp/viewflites.html',{'s2':s2})
                else:
                    return HttpResponse("not")

          else:
            form=flight_search
            return render(request, 'myapp/search_flights.html', {'form': form})

     else:
         form = flight_search
         return render(request, 'myapp/search_flights.html', {'form': form})


from .models import flight_book

def f_book(request):


    if request.session.has_key("username"):
        username = request.session["username"]
        print('h2')
        s = tb_register.objects.filter(email=username)
        l = list(s)
        q = l[0]

        s1 = flight_avail.objects.get()
        a = s1.From
        b = s1.to
        c = s1.arrival
        d = s1.departure
        e = s1.date
        f = s1.category
        g = s1.trip_type
        h = s1.charges

        s1.save()


        s2 = flight_booking(From=a, to=b, arrival=c, departure=d, date=e, category=f, trip_type=g, charges=h, uid=q)
        s2.save()
        return HttpResponse('book')
    else:
        return HttpResponse('not book')


