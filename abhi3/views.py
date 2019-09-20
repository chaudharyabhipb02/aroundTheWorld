from django.shortcuts import render
from .form import emp, DocumentForm
from .form import LoginForm1
from .form import RegistrationForm1
from .models import tb_registrations
from .models import employee, DOCUMENT
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import datetime
today=datetime.datetime.now()
def welcome_page(request):
    text= "<p>this is ahome page<p/>"
    return HttpResponse(text)
def new_page(request):
        return render(request, 'abhi3/page.html', {'name': 'abhi', 'date_value':today})
def registrations(request):
    if request.method=='POST':

        form = RegistrationForm1(request.POST)
        if form.is_valid():
            name1=form.cleaned_data["name"]
            email1=form.cleaned_data["email"]
            contact1 = form.cleaned_data["contact"]
            address1 = form.cleaned_data["address"]
            password1 = form.cleaned_data["password"]
            gender1 = form.cleaned_data["gender"]
            p=tb_registrations(name = name1,email=email1,contact=contact1,address=address1,password=password1,gender=gender1)
            p.save()
            print("this is the valid data from the form",gender1)
            return render(request, "abhi3/done.html", {'name': name1, 'email': email1,'address':address1})

        else:
            return render(request, "abhi3/page.html", {'form':form})
    else:
        form =RegistrationForm1()
        return render(request, "abhi3/page.html", {'form':form})


def login(request):
    if request.method == 'POST':
        form = LoginForm1(request.POST)
        if form.is_valid():
            u_email=form.cleaned_data["email"]
            u_password = form.cleaned_data["password"]
            p=tb_registrations.objects.filter(email=u_email,password=u_password)
            if(p.count()>0):
                request.session['username']=u_email
                print("valid username",p)
                return HttpResponseRedirect('app/thanks')
            else:
                print('try again',p)
                return HttpResponseNotFound('<h1>no page here</h1>')
        else:
            print("\n\n this is else block:{0}\n\n")
            return render(request,"abhi3/login.html",{'form':form})
    else:
        form=LoginForm1()
        print("\n\n tis is else block:{0}\n\n")
        return render(request,"abhi3/login.html",{"form":form})

def template_thanks(request):
    return render(request,"abhi3/thanks.html")


def empl(request):
    global username, q, q1

    if request.method=='POST':


        form = emp(request.POST)
        if form.is_valid():

            e_id1=form.cleaned_data["e_id"]
            e_salary1=form.cleaned_data["e_salary"]
            e_exp1 = form.cleaned_data["e_exp"]
            e_profile1 = form.cleaned_data["e_profile"]

            if request.session.has_key('username'):
                username = request.session['username']

                if request.method == 'POST':

                    form = RegistrationForm1(request.POST)
                    if form.is_valid():
                        name1 = form.cleaned_data["name"]
                        email1 = form.cleaned_data["email"]
                        contact1 = form.cleaned_data["contact"]
                        address1 = form.cleaned_data["address"]
                        password1 = form.cleaned_data["password"]
                        gender1 = form.cleaned_data["gender"]



                        p = tb_registrations.objects.filter(email=email1)
                        p.save()
                        if (p.count() > 0):
                            request.session['username'] = email1
                            print("valid username", p)
                            l = list(p)
                            q = l[0]
                        q1=form.cleaned_data[q]

            p =employee(e_id=e_id1, e_salary=e_salary1, e_exp=e_exp1, e_profile=e_profile1, e_detail=q1)
            p.save()

            return render(request, "abhi3/page.html", {'e_id': e_id1, 'e_salary': e_salary1, 'e_exp': e_exp1, 'e_profile':e_profile1, 'e_detail':q1})

        else:

            return render(request, "abhi3/page.html", {'form': form})
    else:
        form = emp()
        return render(request, "abhi3/page.html", {'form': form})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/display')
    else:
        form = DocumentForm()
    return render(request, 'abhi3/model_form_upload.html', {
        'form': form
    })


x1 = None


def Display_Image(request):
    p = DOCUMENT.objects.filter(description='My pic2').values('document')
    for x in p:
        print(x['document'])
        x1 = x['document']

    return render(request, 'abhi3/display_image.html', {"image": x1})
