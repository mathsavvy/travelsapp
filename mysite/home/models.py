from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50)
    reg_no = models.CharField(max_length=9)
    passwd = models.CharField(max_length=20)
    mob_no = models.IntegerField(default=0)
    alt_mob = models.IntegerField(default=0)

    def __str__(self):
        return self.name