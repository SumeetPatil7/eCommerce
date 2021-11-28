from django.db import models

class Products(models.Model):
    
    name = models.CharField(max_length=255,null=False)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField(max_length=255,null=False)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.name
    