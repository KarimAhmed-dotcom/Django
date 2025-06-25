from django.db import models

# Create your models here.
# title, desc, rate, views	
class Store(models.Model):
    title=models.CharField("book_name",max_length=50)
    description=models.TextField("book_description")
    rate=models.DecimalField(decimal_places=1,max_digits=3)
    views=models.IntegerField()