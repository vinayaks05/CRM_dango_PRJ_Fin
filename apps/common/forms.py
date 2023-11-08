from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.userprofile.models import Profile

# new changes
from .models import *
#from django import forms
from django.forms import ModelForm
# till here

class SignUpForm(UserCreationForm):

    full_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
            #removed password from here as
            #muliple boxes were shown
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

# new change Here
class ContactForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widget ={
                   "name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "phone":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "email":forms.TextInput(attrs={'class': "form-control form-control-sm"}),

                }

class Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widget ={
                   "product":forms.Select(attrs={'class': "form-control form-control-sm"}),
                   "customer":forms.Select(attrs={'class': "form-control form-control-sm"}),
                   "status":forms.Select(attrs={'class': "form-control form-control-sm"}),
                }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widget ={
                   "name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "product":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "vendor":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "discount":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "cost":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                }
