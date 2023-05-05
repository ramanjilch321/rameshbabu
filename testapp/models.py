from django.db import models

# Create your models here.
class Logo_Image(models.Model):
    img = models.CharField(max_length=100)
    n1 = models.CharField(max_length=100)
    n2 = models.CharField(max_length=100)
    n3 = models.CharField(max_length=100)
    n4 = models.CharField(max_length=100)
    contenth1 = models.CharField(max_length=100,default='Design your website')
    contentp1 = models.CharField(max_length=250,default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus repellat repellendus')
    contentp2 = models.CharField(max_length=250,default='optio numquam totam placeat animi site.')
    button2 = models.CharField(max_length=250,default='More')
    button1 = models.CharField(max_length=250,default='Contact')

class Contact_Info(models.Model):
    mobile_number = models.IntegerField(default='9876543210')
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Students_new(models.Model):
    title = models.CharField(max_length=200)
    t1 = models.CharField(max_length=200)
    t2 = models.CharField(max_length=200)
    img = models.CharField(max_length=200)