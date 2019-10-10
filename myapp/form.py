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



