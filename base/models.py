from django.db import models
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


def __str__(self):
    return self.Pick_Up


class Car(models.Model):
    
    Brand_Name = models.CharField(max_length = 200)
    Mod_Name = models.CharField(max_length = 200)
    Desc = models.TextField(max_length = 500)
    Price = models.FloatField()
    Plate_number = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images') 
    status = models.CharField(max_length = 200,null = True)

    def __str__(self):
        return self.Brand_Name

GENDER = (
            ('male', 'male'),
            ('female', 'female'),
    )

class Customer(models.Model):

    car_user = models.ForeignKey(Car, on_delete=models.PROTECT,related_name='cars')
    Name = models.CharField(max_length = 200)
    Age = models.IntegerField()
    Address =  models.CharField(max_length = 200)
    email =  models.CharField(max_length = 200)
    Contact_Number = models.IntegerField()
    License_Number = models.CharField(max_length = 11)
    gender = models.CharField(max_length=9, choices = GENDER, verbose_name = "gender")

    def __str__(self):
        return self.Name

class Booking(models.Model):
    customer_booking = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name='book')
    Pick_Up =  models.CharField(max_length = 200)
    Drop_Off =  models.CharField(max_length = 200)

    def __str__(self):
        return self.Pick_Up


