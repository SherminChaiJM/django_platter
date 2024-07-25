from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User, DistrictOfficeList, BranchLocation

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {"class": "form-control"}
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {"class": "form-control"}
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "is_headoffice", "is_districtoffice", "is_branchlocation")
        widgets = {
            'is_headoffice': forms.CheckboxInput(attrs={'name': 'office'}),
            'is_districtoffice': forms.CheckboxInput(attrs={'name': 'office'}),
            'is_branchlocation': forms.CheckboxInput(attrs={'name': 'office'}),
        }

class DistrictOfficeForm(forms.ModelForm):
    class Meta:
        model = DistrictOfficeList
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'District Office Name'})
        }
        
class BranchLocationForm(forms.ModelForm):
    class Meta:
        model = BranchLocation
        fields = ['districtofficelist', 'text']
        widgets = {
            'districtofficelist': forms.Select(),
            'text': forms.TextInput(attrs={'placeholder': 'Branch Location Name'})
        }