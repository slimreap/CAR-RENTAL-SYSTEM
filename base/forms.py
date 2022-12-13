from django.forms import ModelForm
from .models import Customer,Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class Customer_Form(ModelForm):
    Name = forms.CharField(max_length = 200, required = False)
    Age = forms.IntegerField(required = False)
    Address =  forms.CharField(max_length = 200, required = False)
    email =  forms.CharField(max_length = 200, required = False)
    Contact_Number = forms.IntegerField(required = False)
    License_Number = forms.CharField(max_length = 11, required = False)
    gender = forms.CharField(max_length=9, required = False)  
    class Meta:  
        model = Customer
        fields = ['Name', 'Age', 'Address', 'email', 'Contact_Number', 'License_Number', 'gender']

class PicknDropForm(ModelForm):
    Pick_Up =  forms.CharField(max_length = 200, required = False)
    Drop_Off =  forms.CharField(max_length = 200, required = False)
    class Meta:
        model = Booking
        fields = ['Pick_Up','Drop_Off']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


