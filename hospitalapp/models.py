from django.db import models

# Create your models here.
class users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    yearofbirth = models.DateField(null=True)

    def __str__(self):
        return self.fullname

class product(models.Model):
    product_name = models. CharField(max_length=200)
    product_price = models.CharField(max_length=100)
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

class member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name



