from django import forms
from .models import Product,Order

class ProductForm(forms.ModelForm):
    image=forms.ImageField()
    class Meta:
        model=Product
        fields=[
            'title',
            'description',
            'price',
            'quantity',
            'category',
            'created_by',
        ]
    def save(self, commit=True):
        data=self.cleaned_data
        return Product.objects.create(
        title=data.get('title'),
        description=data.get('description'),
        price=data.get('price'),
        quantity=data.get('quantity'),
        category=data.get('category'),
        image=data.get('image'),
        created_by=data.get('created_by')
        )


    def clean_price(self):
        price=self.cleaned_data.get('price')
        if not price>0:
            raise forms.ValidationError('Price should be more than 0')
        return price

    def clean_quantity(self):
        quantity=self.cleaned_data.get('price')
        if not quantity>=1:
            raise forms.ValidationError('Quantity should be 1 or more')
        return quantity

    def clean_image(self):
        image=self.cleaned_data.get('image')
        max_size=2*1024*1024
        if image.size>max_size:
            raise forms.ValidationError("Image should be less than 2 MB")
        return image

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=[
            'product',
            'count',
        ]
    def save(self, commit=True):
        data=self.cleaned_data
        total_price=data.get('price')*data.get('count')
        return Order.objects.create(
            total_price=total_price,
            user=data.get('user'),
            product=data.get('product'),
            count=data.ketganri
        )