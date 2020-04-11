from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    CITY_CHOICES = [
    ("gandhinagar", "Gandhinagar"),
    ("ahmedabad", "Ahmedabad"),
    ("bhavnagar", "Bhavnagar"),
    ]

    AREA_CHOICES = [
    ("gota", "Gota"),
    ("vaishnodevi", "Vaishnodevi"),
    ("godhrej", "Godhrej Garden City"),
    ]

    RATING_CHOICES = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
    ]

    hostel_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100, default = "UNK")

    area = models.CharField(max_length=20, choices=AREA_CHOICES, default = "UNK") 
    city = models.CharField(max_length=20, choices=CITY_CHOICES, default = "UNK") 
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default = "UNK")


    date_posted = models.DateTimeField(
        default=timezone.now
    )  # only when post was created use--> auto_now_add=True
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hostel_name

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
