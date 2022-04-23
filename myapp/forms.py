from django import forms
from .models import userprofile
from captcha.fields import CaptchaField
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
import re

class profile(forms.ModelForm):
    phonenumber = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="IN"))
    captcha = CaptchaField()

    class Meta:
        model=userprofile
        fields=[
            'firstname',
            'lastname',
            'email',
            'phonenumber',
            'country',
            'password',
            'captcha',
        ]
        widgets={
            'country':forms.Select(attrs={'class':'form-control',"placeholder":"Country"}),
            'phonenumber_0':forms.Select(attrs={'class':'form-control'}),
            'phonenumber_1':forms.TextInput(attrs={'class':'form-control'}),
        }

        # def clean(self):
        #     super(PostForm, self).clean()
        #     password = self.cleaned_data.get('password')
        #     reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        #     pat = re.compile(reg)# searching regex
        #     mat = re.search(pat, password)
        #     # validating conditions
        #     if not mat:
        #         raise forms.ValidationError("This email is already used")
        #
        #     return password



class loginform(forms.Form):
    email=forms.EmailField()
    # firstname=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    class Meta:
        model=userprofile
        fields=[
            "email",
            "password",
        ]
#
#
# class test1(forms.Form):
#     d=userprofile.objects.all().filter(email='q@q.com').values()
#
#     GEEKS_CHOICES=((i,j["firstname"]) for i,j in enumerate(d))
#
#     g=forms.ChoiceField(choices=GEEKS_CHOICES)
# class test1(forms.Form):
#     email=forms.EmailField()

# class ut(forms.Form):
#     # d = userprofile.objects.all().filter(email=email).values()
#
#     GEEKS_CHOICES=((i,j["firstname"]) for i,j in enumerate(d))
#     #
#     g=forms.ChoiceField(choices=GEEKS_CHOICES)
#
