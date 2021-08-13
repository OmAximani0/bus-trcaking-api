from datetime import time
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.

class CustomerUserManager(BaseUserManager):
    
    def create_user(self, password,**extra_fields):
        print("create user called")
        """
        Create and save a User with the given email and password.
        """
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        print("create super user called")
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))    
   
        return self.create_user(password,**extra_fields)
             


class Users(AbstractUser):

    objects = CustomerUserManager()
    first_name = None
    last_name = None
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    


    class Meta:
        db_table = 'users'
        verbose_name_plural = "users"
      




        
