from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django.forms.widgets import FileInput
import re

class UserRegistrationForm(UserCreationForm):
    nickname = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}, format='%m/%d/%Y'), label="Date of Birth")
    avatar = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            self.fields['password'].widget = forms.PasswordInput()
        if 'password_confirm' in self.fields:
            self.fields['password_confirm'] = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'nickname',
            'email',
            'phone',
            'dob',
            'avatar',
            Field('password', css_class='form-control'),
            Field('password_confirm', css_class='form-control'),
            Submit('submit', 'Register', css_class='btn btn-primary')
        )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('nickname', 'email', 'phone', 'dob', 'avatar')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserProfile.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_regex = r'^\+?1?\s*\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'

        if not re.match(phone_regex, phone):
            raise ValidationError("Enter a valid phone number.")
        return phone

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords do not match.")
        return password_confirm
    
    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            if avatar.size > 2 * 1024 * 1024:
                raise ValidationError("Avatar size must be less than 2MB.")
        return avatar

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                nickname=self.cleaned_data['nickname'],
                email=self.cleaned_data['email'],
                phone=self.cleaned_data['phone'],
                dob=self.cleaned_data['dob'],
                avatar=self.cleaned_data['avatar']
            )
        return user

class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    avatar = forms.ImageField(label="Change Avatar", required=False, widget=FileInput)

    class Meta:
        model = UserProfile
        fields = ['nickname', 'email', 'phone', 'dob', 'avatar']

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            if avatar.size > 2 * 1024 * 1024:
                raise ValidationError("Avatar size must be less than 2MB.")
        return avatar
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_regex = r'^\+?1?\s*\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'

        if not re.match(phone_regex, phone):
            raise ValidationError("Enter a valid phone number.")
        return phone