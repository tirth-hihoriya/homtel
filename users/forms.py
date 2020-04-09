from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

CITY_CHOICES = [
    ("gandhinagar", "Gandhinagar"),
    ("ahmedabad", "Ahmedabad"),
    ("bhavnagar", "Bhavnagar"),
]

STATE_CHOICES = [
    ("gujarat", "Gujarat"),
    ("rajasthan", "Rajasthan"),
    ("mumbai", "Mumbai"),
]

COUNTRY_CHOICES = [
    ("desi", "India"),
    ("mate", "Australia"),
    ("sunidhi", "Mars"),
]

ROLE_CHOICES = [
    ("user", "User"),
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
    role = forms.CharField(
        label="Select your role", widget=forms.RadioSelect(choices=ROLE_CHOICES)
    )
    age = forms.IntegerField(max_value=100, min_value=17)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "city",
            "state",
            "country",
            "age",
            "role",
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # default : required=True

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
