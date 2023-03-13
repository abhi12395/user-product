from django.db import models

class productMain(models.Model):
    Title = models.CharField(max_length=30,verbose_name='TITLE')
    description = models.TextField()
    Unique_id = models.CharField(max_length=30,unique=True,verbose_name='Unique id')
    price = models.FloatField(verbose_name='price')

class productImage(models.Model):
    product = models.ForeignKey(productMain,on_delete=models.CASCADE,verbose_name='Product Image')
    image = models.ImageField(verbose_name='IMAGE')
