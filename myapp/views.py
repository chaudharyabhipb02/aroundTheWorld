from django.shortcuts import render, redirect
from .form import RegistrationForm1
from .form import LoginForm1, SearchForm
from .model import tb_register
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import requests

def pro(request):
    return render(request, "myapp/index.html")


def about(request):
    return render(request, "myapp/about.html")


def contact(request):
    return render(request, "myapp/contacts.html")


def destination(request):
    return render(request, "myapp/destinations.html")


def tour(request):
    return render(request, "myapp/tours.html")


def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            departure = form.cleaned_data["departure"]
            arrival = form.cleaned_data["arrival"]
            date = form.cleaned_data["date"]
            request.session["departure"] = departure
            request.session["arrival"] = arrival
            request.session["date"] = date

        else:
            return HttpResponse("Not valid")
        return redirect('/flight')
    else:
        form = SearchForm()
        return render(request, 'myapp/home.html', {"form": form})


def register(request):
    if request.method == 'POST':

        form = RegistrationForm1(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data["name"]
            email1 = form.cleaned_data["email"]
            contact1 = form.cleaned_data["contact"]
            address1 = form.cleaned_data["address"]
            password1 = form.cleaned_data["password"]
            gender = form.cleaned_data["gender"]
            p = tb_register(name=name1, email=email1, contact=contact1, address=address1, password=password1, gender=gender)
            p.save()
            return HttpResponseRedirect('myapp/login')

        else:
            return render(request, "myapp/form.html", {'form': form})
    else:
        form = RegistrationForm1()
        return render(request, "myapp/form.html", {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm1(request.POST)
        if form.is_valid():
            u_email = form.cleaned_data["email"]
            u_password = form.cleaned_data["password"]
            p = tb_register.objects.filter(email=u_email, password=u_password)
            if p.count() > 0:
                request.session['username'] = u_email
                return HttpResponseRedirect("sss")
            else:
                print('try again', p)
                return HttpResponseNotFound('<h1>no page here</h1>')
        else:
            print("\n\n this is else block:{0}\n\n")
            return render(request, "myapp/login.html", {'form': form})
    else:
        form = LoginForm1()
        print("\n\n tis is else block:{0}\n\n")
        return render(request, "myapp/login.html", {"form": form})


def sis(request):
    if request.session.has_key("username"):
        username = request.session["username"]
    return render(request, "myapp/done.html", {"username": username})


def flight_search(request):
    objects = requests.get('http://127.0.0.1:5000/api/flights/find/{}/{}/'.format(request.session["departure"], request.session["arrival"]))
    fetched_data = objects.json()
    return render(request, "myapp/flightData.html", {"flights": fetched_data})
