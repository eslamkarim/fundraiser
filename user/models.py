from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_email_address = models.EmailField()
    user_password = models.CharField(max_length=250)
    sign_up_date = models.DateTimeField(auto_now_add=True, blank=True)
    verification_code = models.IntegerField()
    is_verified_user = models.BooleanField(default=False)


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    project_owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_target = models.IntegerField()
    donation_amount = models.IntegerField()
    donations = models.ManyToManyField(User, related_name="donations")