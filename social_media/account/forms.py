from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Profile

messages={

          "required": 'این فیلد اجباری است',
          "invalid" : 'ایمیل معتعبر نیست'



}


class UserLoginForm(forms.Form):

    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
    password=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))




class UserRegistrationForm(forms.Form):

   username=forms.CharField(error_messages=messages,max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
   password=forms.CharField(error_messages=messages,max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
   email=forms.EmailField(error_messages=messages,max_length=50,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))



class EditProfileForm(forms.ModelForm):
    email=forms.EmailField(max_length=300)
    class Meta:
        model=Profile
        fields=('bio','age',)


class PhoneLoginForm(forms.Form):

    phone=forms.IntegerField()

    def clean_phone(self):
        phone=Profile.objects.filter(phone=self.cleaned_data['phone'])
        if not phone.exists():
            raise forms.ValidationError('This phone number does not exists')
        return self.cleaned_data['phone']


class VerifyCodeForm(forms.Form):
    code=forms.IntegerField()