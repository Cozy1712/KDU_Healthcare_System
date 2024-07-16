from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Room, RegisterUser, User, Appointment

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Username: e.g. kolawole001",
                "id": "user",
            }
        ),
        
    )
    email = forms.CharField(
        required=True,
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "Email Address: e.g. kola001@gmail.com",
                "id": "email",
            }
        ),
        
    )
    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter your Full Name: e.g. Adebayo Johnson",
                "id": "name",
            }
        ),
        
    )
    card_number = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter the Card Number",
                "id": "card_number",
            }
        ),
        
    )
    gender = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Your Gender",
                "id": "gender",
            }
        ),
        
    )
    password1 = forms.CharField(
        required=True, min_length=8,
        widget=forms.widgets.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                "id": "password",
                "onKeyUp": "check_password_length()",
            }
        ),
        
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.widgets.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "id": "password2",
            }
        ),
        
    )
    class Meta:
        model = User
        fields = [ 'username', 'email','name','card_number','gender']
        exclude = ['status', 'active']

    # def username_clean(self):  
    #     username = self.cleaned_data['username'].lower()  
    #     new = User.objects.filter(username = username)  
    #     if new.count():  
    #         raise ValidationError("User Already Exist")  
    #     return username  
  
    # def email_clean(self):  
    #     email = self.cleaned_data['email'].lower()  
    #     new = User.objects.filter(email=email)  
    #     if new.count():  
    #         raise ValidationError(" Email Already Exist")  
    #     return email  
  
    # def clean_password2(self):  
    #     password1 = self.cleaned_data['password1']  
    #     password2 = self.cleaned_data['password2']  
  
    #     if password1 and password2 and password1 != password2:  
    #         raise ValidationError("Password don't match")  
    #     return password2  
  
    # def save(self, commit = True):  
    #     user = User.objects.create_user(  
    #         self.cleaned_data['username'],  
    #         self.cleaned_data['email'],  
    #         self.cleaned_data['password1']  
    #     )  
    #     return user



class  MyDoctorCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Username: e.g. kolawole001",
                "id": "user",
            }
        ),
        
    )
    email = forms.CharField(
        required=True,
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "Email Address: e.g. kola001@gmail.com",
                "id": "email",
            }
        ),
        
    )
    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter your Full Name: e.g. Adebayo Johnson",
                "id": "name",
            }
        ),
        
    )
  
    gender = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Your Gender",
                "id": "gender",
            }
        ),
        
    )
    password1 = forms.CharField(
        required=True, min_length=8,
        widget=forms.widgets.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                "id": "password",
                "onKeyUp": "check_password_length()",
            }
        ),
        
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.widgets.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "id": "password2",
            }
        ),
        
    )
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'specialisation','gender']
        exclude = ['status', 'active']


class  MyAdminCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Username: e.g. kolawole001",
                "id": "user",
            }
        ),
        
    )
    email = forms.CharField(
        required=True,
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "Email Address: e.g. kola001@gmail.com",
                "id": "email",
            }
        ),
        
    )
    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter your Full Name: e.g. Adebayo Johnson",
                "id": "name",
            }
        ),
        
    )
  
    gender = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Your Gender",
                "id": "gender",
            }
        ),
        
    )
    password1 = forms.CharField(
        required=True, min_length=8,
        widget=forms.widgets.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                "id": "password",
                "onKeyUp": "check_password_length()",
            }
        ),
        
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.widgets.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "id": "password2",
            }
        ),
        
    )
    class Meta:
        model = User
        fields = ['username', 'name', 'email','gender']
        exclude = ['status', 'active']



class RoomForm(ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "maxlength": "24",
                "id": "gender",
            }
        ),
        
    )
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class AppointmentForm(ModelForm):
    date = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "id": "date",
                "type": "date",
            }
        ),
    )
    time = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "id": "time",
                "type": "time",
            }
        ),
    )
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ['user', 'user1','user2','fname']


class UserForm(ModelForm):
    class Meta:
        model = RegisterUser
        fields = '__all__'
        exclude = ['user','status']

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'bio']
        # exclude = ['password1','password2']

class DoctorUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','certificate','name', 'bio']

class UserForm3(ModelForm):
    class Meta:
        model = User
        fields = ['name','card_number','gender']


class DoctorForm(ModelForm):
    class Meta:
        model = RegisterUser
        fields = '__all__'
        exclude = ['user','status']


class UpdateUserForm(ModelForm):
    class Meta:
        model = RegisterUser
        fields = '__all__'
        exclude = ['user','status'] 
