from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    register_number = models.CharField(max_length=9)
    mobile_number = models.IntegerField(max_length=10)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'users'