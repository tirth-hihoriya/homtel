from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms.widgets import DateInput

CITY_CHOICES = [
    ("gandhinagar", "Gandhinagar"),
    ("ahmedabad", "Ahmedabad"),
    ("bhavnagar", "Bhavnagar"),
]

STATE_CHOICES = [
    ("gujarat", "Gujarat"),
    ("rajasthan", "Rajasthan"),
    ("maharastra", "Maharastra"),
]

COUNTRY_CHOICES = [
    ("desi", "India"),
    ("mate", "Australia"),
    ("sunidhi", "USA"),
]

ROLE_CHOICES = [
    ("coustomer", "Customer"),
    ("seller", "Seller"),
]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # default : required=True
    first_name = forms.CharField(
        label="First Name", max_length=50
    )  # default : required=True
    last_name = forms.CharField(
        label="Last Name", max_length=50
    )  # default : required=True
    city = forms.CharField(label="City", widget=forms.Select(choices=CITY_CHOICES))
    state = forms.CharField(label="State", widget=forms.Select(choices=STATE_CHOICES))
    country = forms.CharField(
        label="Country", widget=forms.Select(choices=COUNTRY_CHOICES)
    )
    user_role = forms.CharField(
        label="Are you a Seller/Hostel_Owner or a Coustomer/Student?",
        widget=forms.Select(choices=ROLE_CHOICES),
    )
    contact = forms.CharField(label="Phone No.", max_length=13)

    class DateInput(forms.DateInput):
        input_type = "date"

    dob = forms.DateField(label="Date of Birth", widget=DateInput())

    class Meta:
        model = User
        fields = [
            "user_role",
            "first_name",
            "last_name",
            "city",
            "state",
            "country",
            "dob",
            "username",
            "email",
            "contact",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # default : required=True
    first_name = forms.CharField(
        label="First Name", max_length=50
    )  # default : required=True
    last_name = forms.CharField(
        label="Last Name", max_length=50
    )  # default : required=True
    city = forms.CharField(label="City", widget=forms.Select(choices=CITY_CHOICES))
    state = forms.CharField(label="State", widget=forms.Select(choices=STATE_CHOICES))
    country = forms.CharField(
        label="Country", widget=forms.Select(choices=COUNTRY_CHOICES)
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "city",
            "state",
            "country",
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
