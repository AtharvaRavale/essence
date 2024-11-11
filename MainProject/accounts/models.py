from django.db import models
from django.contrib.auth.models import User

class MyManager(models.Manager):
    def my_query(self):
        return self.all()
    def address(self):
        return self.all().only('user','title')
    def full_address(self):
        return self.all()



# Create your models here.
class Address(models.Model):
    objects=MyManager()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=100)
    address_line1=models.CharField(max_length=100)
    address_line2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    code=models.CharField(max_length=100)



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='customer/profile/img')
    age = models.IntegerField()
    contact_details = models.CharField(max_length=100)
    gender = models.CharField(choices=(('m','male'),('f','female')),max_length=10)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
