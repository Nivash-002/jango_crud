from django.db import models

# Create your models here.
class CrudData(models.Model):
    Name=models.CharField("", max_length=50)
    Age=models.IntegerField()
    Email=models.EmailField("", max_length=254)
    Degree=models.CharField("", max_length=50)
    Passed_out=models.IntegerField()
    
    def __str__(self):
        return self.name