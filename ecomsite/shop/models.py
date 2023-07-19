from django.db import models

# Create your models here.



class Category(models.Model):
    title = models.CharField(verbose_name="الصنف", max_length=200)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "الأصناف"

class Products(models.Model):
    title = models.CharField(verbose_name="اسم المنتج", max_length=200)
    price = models.FloatField(verbose_name="السعر")
    quantity= models.IntegerField(verbose_name="الكمية", null=True, blank=True)
    category = models.ForeignKey(Category, max_length=200, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الصنف")
    description = models.TextField(verbose_name="وصف المنتج")
    discount = models.BooleanField(verbose_name="عليه خسم", null=True, blank=True)
    discount_price = models.FloatField(verbose_name="السعر بعد الخسم")
    image = models.ImageField(verbose_name="صورة المنتج", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "المنتجات"
    



    
  
