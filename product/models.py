from django.db import models

from config.settings import AUTH_USER_MODEL


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()
    image=models.ImageField(upload_to='product/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    created_by=models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='products')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.created_by}'

class Order(models.Model):
    STATUS_CHOICE=[
        ('new','New'),
        ('paid','Paid'),
        ('cancelled','Cancelled'),
    ]
    user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='order')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order')
    count=models.PositiveIntegerField()
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=30,choices=STATUS_CHOICE,default='new')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title} for {self.user.username}'



