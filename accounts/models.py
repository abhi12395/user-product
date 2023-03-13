from django.db import models
from product.models import*


GENDER =[("MALE","MALE"),
         ("FEMALE","FEMALE"),
         ("OTHERS","OTHERS"),
        ]

STATUS = [
    ("PENDING","PENDING"),
    ("COMPLETED","COMPLETED"),
]


class User(models.Model):
    phone_number = models.IntegerField(unique=True,verbose_name='Phone Number')
    email = models.EmailField(verbose_name='Email',null=True)
    is_customer = models.BooleanField()
    is_admin =  models.BooleanField()

class User_Profile(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER, verbose_name='Gender')
    image = models.ImageField(verbose_name='IMAGE')

class login_top(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE ,verbose_name='LOGIN TOP')
    otp = models.IntegerField(verbose_name='OTP')
    active = models.BooleanField(verbose_name='ACTIVE')


class UserCartProduct(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE ,verbose_name='USER CARD PRODUCT')
    product = models.ForeignKey(productMain,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=STATUS,verbose_name='STATUS')

class UserCart(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE )
    products = models.ManyToManyField(UserCartProduct)
    price = models.FloatField(verbose_name='price')
