from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from listings.models import MontUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # email_check = User.objects.filter(email=email)
        # if email_check.exists():
        #     raise forms.ValidationError('This Email already exists')
        if email and not email.endswith('@westmont.edu'):
            raise forms.ValidationError("Only Westmont College email addresses are allowed.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        phone = self.cleaned_data['phone']
        if commit:
            user.save()
            mont_user = MontUser.objects.get_or_create(user=user)[0]
            mont_user.phone = phone
            mont_user.save()
        return user

