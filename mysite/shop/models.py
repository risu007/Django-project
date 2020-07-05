from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name= models.CharField(max_length=9000)
    category=models.CharField(max_length=9000,default="")
    subcategory=models.CharField(max_length=9000,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=9000)
    pub_date = models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=9000,default="")
    email=models.CharField(max_length=9000,default="")
    phone=models.CharField(max_length=9000,default="")
    desc=models.CharField(max_length=9000,default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=9000)
    name= models.CharField(max_length=9000,default="")
    email=models.CharField(max_length=9000,default="")
    phone=models.CharField(max_length=9000,default="")
    address= models.CharField(max_length=1100,default="")
    state=models.CharField(max_length=9000,default="")
    city=models.CharField(max_length=9000,default="")
    zip_code=models.CharField(max_length=9000,default="")
    amount=models.IntegerField(default=0)

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=9000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."
