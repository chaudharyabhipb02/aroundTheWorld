from django.shortcuts import render, redirect
from .form import RegistrationForm1
from .form import LoginForm1, SearchForm
from .model import tb_register
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import requests
from datetime import datetime


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
            date_value = form.cleaned_data["date"]
            print(date_value)
            request.session["departure"] = departure
            request.session["arrival"] = arrival
            request.session["date"] = date_value.strftime("%d/%m/%Y")
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
    state_data_utl = "http://airlabs.co/api/v6/autocomplete?api_key=670d1cf7-b4de-40ae-94c8-2f4f67c0decb&query="
    departure_input = request.session["departure"]
    arrival_input = request.session["arrival"]
    date_value = datetime.strptime(request.session["date"], "%d/%m/%Y")
    departure_state_data = requests.get(state_data_utl + departure_input)
    arrival_state_data = requests.get(state_data_utl + arrival_input)
    date = date_value.strftime("%d")
    month = date_value.strftime("%m")
    year = date_value.strftime("%Y")
    departure_code = departure_state_data.json()["response"]["cities"][0]['code'].lower()
    arrival_code = arrival_state_data.json()["response"]["cities"][0]['code'].lower()
    objects = requests.get('http://127.0.0.1:5000/api/flights/find/{}/{}/{}/{}/{}/'.format
                           (departure_code, arrival_code,
                            year, month, date))
    fetched_data = objects.json()
    custom_data = []
    for flight in fetched_data:
        custom_dict = {
            "departure": departure_state_data.json()["response"]["cities"][0]["name"],
            "arrival": arrival_state_data.json()["response"]["cities"][0]["name"],
            "departure_date": datetime.strptime(flight["departure_date"], "%d/%m/%y").strftime("%d %b %y"),
            "arrival_date": datetime.strptime(flight["arrival_date"], "%d/%m/%y").strftime("%d %b %y"),
            "departure_time": flight["departure_time"],
            "arrival_time": flight["arrival_time"],
            "departure_code": flight["departure"],
            "arrival_code": flight["arrival"],
            "flight_number": flight["flight_number"],
            "image": flight["image"],
            "airline": flight["airline"],
            "price": flight["price"],
            "departure_day": datetime.strptime(flight["departure_date"], "%d/%m/%y").strftime("%a"),
            "arrival_day": datetime.strptime(flight["arrival_date"], "%d/%m/%y").strftime("%a"),
        }

        custom_data.append(custom_dict)
    return render(request, "myapp/flightData.html", {"flights": custom_data})
