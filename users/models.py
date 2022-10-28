from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserModel(AbstractUser):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, _('Male')), (GENDER_FEMALE, _('Female'))]
    user_image = models.ImageField(upload_to='users/', default='main/img/user+icon.png')
    id_card = models.CharField(max_length=9, null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    location_work = models.CharField(max_length=255, null=True, blank=True)
    address_work = models.CharField(max_length=255, null=True, blank=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)