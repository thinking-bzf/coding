from django.shortcuts import render
from .models import Pizza,Topping
# Create your views here.


def index(request):
    return render(request, 'Pizzaxs/index.html')


def Pizzas(request):
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'Pizzaxs/Pizzas.html', context)


def Seasoning(request, pizza_id):
    pizza1 = Topping.objects.get(id = pizza_id)
    seasoning = pizza1.name
    context = {'pizza': pizza1, 'sea': seasoning}
    return render(request, 'Pizzaxs/pizza.html',context)
