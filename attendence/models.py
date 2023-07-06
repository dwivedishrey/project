from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
class CustomUser(AbstractUser):
    staff_id=models.CharField(verbose_name=_("Staff_id"),max_length=30)
    pincode=models.CharField(verbose_name=_("Pincode"),null=True,max_length=30)

class Attendence(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=100,default=0)
    classes=models.ManyToManyField('Class_name', related_name='item')
    phone_number=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Class_name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class date_wise(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.ManyToManyField(
        'Attendence', related_name='order', blank=True)
    def __str__(self):
        return f'Order: {self.created_on.strftime("%Y-%m-%d: %M %p")}'
    class Meta:
        db_table="att"
