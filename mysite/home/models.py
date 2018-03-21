from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Extra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=9)
    mob_no = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email