# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# class User(models.Model):
#     username=models.CharField(max_length=100, blank=False)
#     password=models.CharField(max_length=100, blank=False)

class Contacts(models.Model):
    contact_name = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

