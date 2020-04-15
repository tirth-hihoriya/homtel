from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .models import Post,RoomCategory
from django.forms.widgets import DateInput

class HostelUpdateForm(forms.Modelform):
    model = Post
    fields = [
        "hostel_name",
        "address",
        "area",
        "city",
        "contact",
        "rating",
        "breakfast",
        "lunch",
        "dinner",
        "transportation",
        "cctv",
        "fridge",
        "washing_machine",
        "geyser",
        "ac",
        "author"
    ]