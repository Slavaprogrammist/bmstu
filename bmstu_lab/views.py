"""from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from bmstu_lab.models import arendaavto

def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Camry 3.5', 'id': 1},
            {'title': 'Lambo Urus', 'id': 2},
            {'title': 'Новый Мерин', 'id': 3},
        ]
    }})
def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})

def carList(request):
    return render(request, 'cars.html', {'data' : {
        'current_date': date.today(),
        'cars': Car.objects.all()
    }})

def GetCar(request, id):
    return render(request, 'car.html', {'data' : {
        'current_date': date.today(),
        'book': Car.objects.filter(id=id)[0]
    }})"""
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

def GetData():
    return [
        {'title': 'Автомобиль №1', 'id': 1,
         'description': 'Camry 3.5',
         'power': '277 л.с.',
         'price': '7000 рублей'},

        {'title': 'Автомобиль №2', 'id': 2,
         'description': 'Lambo Urus',
         'power': '650 л.с.',
         'price': '15000 рублей'},

        {'title': 'Автомобиль №3', 'id': 3,
         'description': 'Mersedes Benz E200',
         'power': '197 л.с.',
         'price': '10000 рублей'}
    ]



def hello(request):
    return HttpResponse('Hello world!')

def hello(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'index.html', {
        'current_date': date.today()
    })

def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'cars': GetData()
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        'cars': GetData()

    }})
