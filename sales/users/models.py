from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    website = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
    
    
class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s OTP"

