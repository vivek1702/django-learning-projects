from django.db import models

# Create your models here.

class person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=10, default="male")
    age = models.IntegerField()
    profile_photo = models.FileField(upload_to="files/")
    created_at = models.DateTimeField(auto_now_add=True)

