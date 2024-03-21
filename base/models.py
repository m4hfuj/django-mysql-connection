from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    address = models.CharField(max_length=256,  blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    amount = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['price']
    
    def __str__(self):
        return self.product_name
    

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_amount = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
