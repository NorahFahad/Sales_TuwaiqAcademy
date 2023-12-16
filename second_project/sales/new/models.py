from django.db import models

class Customers(models.Model):
   id = models.IntegerField(primary_key=True)
   FirstName = models.CharField(max_length=100)
   LastName = models.CharField(max_length=100)

   def __str__(self):
       return self.id


class Products(models.Model):
   id = models.IntegerField(primary_key=True)
   Name = models.CharField(max_length=100)
   Price = models.CharField(max_length=100)

   def __str__(self):
       return self.id


class Orders(models.Model):
   id = models.IntegerField(primary_key=True)
   CustomerID  = models.ForeignKey(Customers, on_delete=models.CASCADE)
   ProductsID = models.ForeignKey(Products, on_delete=models.CASCADE)
   Quantity = models.CharField(max_length=100)
   CreatedAt = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.id


class Reviews(models.Model):
   id = models.IntegerField(primary_key=True)
   CustomerID  = models.ForeignKey(Customers, on_delete=models.CASCADE)
   ProductsID = models.ForeignKey(Products, on_delete=models.CASCADE)
   Rating = models.CharField(max_length=100)
   Review = models.CharField(max_length=100)

   def __str__(self):
       return self.id