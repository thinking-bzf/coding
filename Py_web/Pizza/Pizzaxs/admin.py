from django.contrib import admin

# Register your models here.
from Pizzaxs.models import Pizza,Topping
admin.site.register(Pizza)
admin.site.register(Topping)