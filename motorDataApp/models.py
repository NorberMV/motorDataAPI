
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class MotorData(models.Model):
    """Modeling the main characteristics from a electric motor. """
     
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=600, null=True, blank=False) #widget=forms.Textarea
    
    # Fixed choice fields
    power = models.CharField(max_length=10, null=True, blank=True)
    speed = models.CharField(max_length=10, null=True)
    phases_number = models.CharField(max_length=10, null=True)
    purpose = models.CharField(max_length=15, null=True)
    applications = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = ('Motor Data') # In order to quit the plural 's in the admin panel

    def __str__(self):
        return self.name # This variable is going to be visible when I make a query
    
    # This decorator avoid the error when an image file is empty
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
            if url == '':
                url = ''
        return url