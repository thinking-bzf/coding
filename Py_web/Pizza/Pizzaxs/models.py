from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.TextField()
    
    def __str__(self):
        if len(self.name) > 10:
            return self.name[:10] + '...'
        else:
            return self.name
