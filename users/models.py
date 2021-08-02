from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(upload_to="user/profile_photos", null=True, blank=True)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, null=True, blank=True)
    birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    voucher = models.BooleanField(default=False)
    end_of_voucher = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
