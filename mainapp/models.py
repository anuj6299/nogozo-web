from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=20)
    comment = models.TextField()
    
    def __str__(self):
        return self.name


class MerchantFeedback(models.Model):
    shop_name = models.CharField(max_length=120)
    contact_number = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=250)
    comment = models.TextField()
    
    def __str__(self):
        return self.shop_name

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.city_name

        
class Area(models.Model):
    area_id = models.IntegerField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=500)

    def __str__(self):
        return self.area_name

class Shop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=500)

    def __str__(self):
        return self.shop_name

class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500)

    def __str__(self):
        return self.item_name


