from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_email_address = models.EmailField()
    user_password = models.CharField(max_length=250)
    sign_up_date = models.DateTimeField(auto_now_add=True, blank=True)
    verification_code = models.CharField(max_length=20)
    is_verified_user = models.BooleanField(default=False)