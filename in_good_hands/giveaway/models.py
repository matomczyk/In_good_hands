from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)


class Institution(models.Model):
    TYPE = (
        (1, "fundation"),
        (2, "non-governmental organization"),
        (3, "local")
    )
    name = models.CharField(max_length=122)
    description = models.CharField()
    type = models.IntegerField(choices=TYPE, default=1)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=122)
    phone_number = models.IntegerField()
    city = models.CharField()
    zip_code = models.CharField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

