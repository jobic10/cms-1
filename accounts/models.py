from asyncio.windows_events import NULL
from itertools import product
from django.db import models
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import AbstractUser,UserManager


# Create your models here.
class CustomUserManager(UserManager):

    def _create_user(self,email,password, **extra_fields):
        email=self.normalize_email(email)
        user=CustomUser(email=email, **extra_fields)
        user.password = make_password(password) # hash the password 
        user.save(using=self._db)
        return user

    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self,email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('user_type',1)
        extra_fields.setdefault('last_name', 'System')
        extra_fields.setdefault('first_name', 'Administrator')

        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']
        return self._create_user(email,password,**extra_fields)


        

class CustomUser(AbstractUser):
    USER_TYPE=((1,'Admin'),(2,'cms'))
    username=None #use email instead of username
    email=models.EmailField(unique=True)
    user_type=models.CharField(default=1,choices=USER_TYPE,max_length=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []
    objects=CustomUserManager()

    def __str__(self):
        return self.last_name + '' + self.first_name

class Customer(models.Model):
    profile=models.ImageField(null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    surname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    phone=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField()
    category=models.CharField(max_length=255,null=True,choices=CATEGORY)
    description=models.CharField(max_length=255,null=True,blank=True)
    tags=models.ManyToManyField(Tag)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
        ('Delivered','Delivered'),
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery')
    )
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    note=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=100,null=True,choices=STATUS)

    def __str__(self):
        return self.product.name

    




   