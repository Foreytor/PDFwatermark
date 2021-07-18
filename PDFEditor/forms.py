from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from PDFEditor.models import *

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AddECP(forms.ModelForm):
    class Meta:
        model = ECP
        # fields = '__all__'
        fields = ['name', 'pathESP',]


class SuperimposeFrom(forms.ModelForm):
    class Meta:
        model = Wotermark
        # fields = '__all__'
        fields = ['pathOld', 'pathNew']
        '''widgets = {
            'pathNew': forms.ModelChoiceField(queryset=Wotermark.objects.filter(user_main=request.user)),
        }   '''     

    def __init__ (self, *args, **kwargs):
        # Call the constructor form and maintain user

        user = kwargs.pop('user')
        qs = ECP.objects.filter(user_main__id=user.id)

        super(SuperimposeFrom, self).__init__(*args, **kwargs)
        print(self.fields)
        self.fields['pathNew'].queryset = qs
    



