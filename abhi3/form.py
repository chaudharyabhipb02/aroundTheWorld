from django import forms
from.models import DOCUMENT
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


class emp(forms.Form):
    e_id = forms.CharField(label="Enter employee id", max_length=200)
    e_salary = forms.CharField(label="Enter employee salary", max_length=200)
    e_exp = forms.CharField(label="Enter employee experiance", max_length=200)
    e_profile = forms.CharField(label="Enter profile", max_length=200)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = DOCUMENT
        fields = ('description', 'document', )



