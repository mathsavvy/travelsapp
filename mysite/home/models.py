from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Extra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=9)
    mob_no = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email

class CabRide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup = models.CharField(max_length=100)
    drop = models.CharField(max_length=100)
    time = models.TimeField(default=timezone.now)
    def __str__(self):
        return self.user.first_name + " " + self.drop 