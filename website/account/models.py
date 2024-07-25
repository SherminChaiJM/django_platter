from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_headoffice = models.BooleanField('Is Head Office', default=False)
    is_districtoffice = models.BooleanField('Is District Office', default=False)
    is_branchlocation = models.BooleanField('Is Branch Location', default=False)
    
    class Meta:
        permissions = [
            ('view_headoffice', 'Can view head office website'),
            ('view_districtoffice', 'Can view district office website'),
            ('view_branchlocation', 'Can view branch location website'),
        ]
        
        
class DistrictOfficeList(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class BranchLocation(models.Model):
    districtofficelist = models.ForeignKey(DistrictOfficeList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    
    def __str__(self):
        return self.text