from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) #lock this profile to a user. 
    account_number = models.CharField(max_length=26)
    address = models.CharField(max_length=100,blank = True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now = True)
    #avatar =
    
    def __str__(self):
        return f"Profile of the user: {self.user.username}"
 