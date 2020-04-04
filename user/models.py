from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def _create_user(self, **extra_fields):
        print(extra_fields)
        print("############################################################################################################################################################################################")
        user = Profile(
            user_email_address=extra_fields['email'],
            user_first_name=extra_fields['first_name'],
            user_last_name=extra_fields['last_name'],
            is_verified_user=True,

        )
        user.save()
        return user


    def create_user(self, **extra_fields):
        return self._create_user(**extra_fields)

# Create your models here.
class Profile(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_email_address = models.EmailField(blank=True)
    user_phone_number=models.CharField(max_length=20)
    user_birthDate=models.DateField(null=True)
    user_country=models.CharField(max_length=50)
    user_password = models.CharField(max_length=250)
    sign_up_date = models.DateTimeField(auto_now_add=True, blank=True)
    verification_code = models.CharField(max_length=20)
    is_verified_user = models.BooleanField(default=False)
    username = models.CharField(max_length=20, blank=True)
    last_login = models.DateTimeField(null=True)
    is_authenticated = models.BooleanField(default=False)
    objects = MyUserManager()