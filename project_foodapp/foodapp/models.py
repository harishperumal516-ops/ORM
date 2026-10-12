from django.db import models

# Create your models here.
class foodapp(models.Model):
    customer_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    is_allowed = models.BooleanField(default=True)