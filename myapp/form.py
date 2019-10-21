from django import forms
class RegistrationForm1(forms.Form):
    name = forms.CharField(label="Enter Your Name", max_length=200)
    email = forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    contact = forms.CharField(label="Enter Your Contact", max_length=200)
    address = forms.CharField(label="Enter Your Address", max_length=200)
    password = forms.CharField(label="Enter Your Password", max_length=200,widget=forms.PasswordInput)

    CHOICES=[('male','male'),('female','female')]

    gender=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

class LoginForm1(forms.Form):
    email = forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    password = forms.CharField(label="Enter Your password", max_length=200)


class feedbackform(forms.Form):
    name = forms.CharField(label="Enter your name",max_length=100)
    message = forms.CharField(label="Enter your message",max_length=100)
    image = forms.ImageField(label="Enter image",required=False)
class flight_available(forms.Form):
    From = forms.CharField(label="from",max_length=100)
    to = forms.CharField(label="to",max_length=100)
    arrival = forms.CharField(label="Arrival",max_length=100)
    departure = forms.CharField(label="Departure",max_length=100)
    date = forms.CharField(label="date",max_length=100)
    CHOICES = [('economy class','economy class'), ('bussiness class', 'bussiness class')]
    category = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    CHOICES = [('round trip', 'round trip'), ('one way', 'one way')]
    trip_type = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    charges = forms.CharField(label="Charges",max_length=100)

class flight_search(forms.Form):
    From = forms.CharField(label="from", max_length=100)
    to = forms.CharField(label="to", max_length=100)
    date = forms.CharField(label="date", max_length=100)
    CHOICE = [('economy class', 'economy class'), ('bussiness class', 'bussiness class')]
    category = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect)
    CHOICES = [('round trip', 'round trip'), ('one way', 'one way')]
    trip_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
class flight_booking(forms.Form):
    From = forms.CharField(label="from", max_length=100)
    to = forms.CharField(label="to", max_length=100)
    arrival = forms.CharField(label="Arrival", max_length=100)
    departure = forms.CharField(label="Departure", max_length=100)
    date = forms.CharField(label="date", max_length=100)
    CHOICES = [('economy class', 'economy class'), ('bussiness class', 'bussiness class')]
    category = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    CHOICES = [('round trip', 'round trip'), ('one way', 'one way')]
    trip_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    charges = forms.CharField(label="Charges", max_length=100)

class flight_payment(forms.Form):
    costing = forms.CharField(label="Costing", max_length=100)
    CHOICES = [('DEBIT CARD', 'DEBIT CARD'), ('CREDIT CARD', 'CREDIT CARD'), ('ONLINE TRANSACTION', 'ONLINE TRANSACTION')]
    payment_mode = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    booking_date = forms.CharField(label="Booking date", max_length=100)

