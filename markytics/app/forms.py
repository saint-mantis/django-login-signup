from django import forms
from .models import User



class LoginForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(LoginForm, self).__init__(*args, **kwargs)
         self.fields['username'].widget.attrs.update({'id':'uname','class': 'form-control','placeholder':'enter your username'})
         self.fields['password'].widget.attrs.update({'id':'pwd','class': 'form-control','placeholder':'enter your password'})
    
     class Meta:
        model = User
        labels = {
            'username': '',
            'password': '',
        }
        widgets = {

            'password': forms.PasswordInput() 
        }
        fields = ['username', 'password']



class SignupForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(SignupForm, self).__init__(*args, **kwargs)
         self.fields['username'].widget.attrs.update({'id':'','class': 'form-control','placeholder':'Username'})
         self.fields['email'].widget.attrs.update({'id':'','class': 'form-control','placeholder':'Email'})
         self.fields['password'].widget.attrs.update({'id':'','class': 'form-control','placeholder':'Password'})
    
     class Meta:
        model = User
        labels = {
            'username': '',
            'password': '',
            'email': '',
        }
        widgets = {
            
            'password': forms.PasswordInput() 
        }
        fields = ['username', 'password','email']
       
