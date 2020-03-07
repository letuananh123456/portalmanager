from django import forms
from .models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, 
    widget=forms.TextInput(attrs={'class': 'input100', 'placeholder':'Số điện thoại'}))
    password = forms.CharField(max_length=50, required=True, 
    widget=forms.TextInput(attrs={'type': 'password', 'class': 'input100', 'placeholder':'Mật khẩu'}))

class ProfileForm(forms.ModelForm):

    # GIOITINH = (('0','Nữ'),('1','Nam'))
    # hoten = forms.CharField(max_length=225, required=True)
    # cmnd = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control'}))
    # ngaysinh = forms.DateField(input_formats='%d/%m/%Y',required=True,widget=DateInput())
    # gioitinh = forms.ChoiceField(required=True,widget=forms.SelectMultiple,choices=GIOITINH)

    class Meta:
        model = User
        fields = ['hoten','cmnd','ngaysinh','gioitinh']


        



