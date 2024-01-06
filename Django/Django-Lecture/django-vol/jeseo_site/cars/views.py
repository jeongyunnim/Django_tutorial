from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.

def list(request):
    all_car = models.Cars.objects.all()
    context = {"all_cars":all_car}
    return (render(request, 'cars/list.html', context=context))

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Cars.objects.create(brand=brand, year=year)
        return (redirect(reverse("cars:list")))
    else:
        return (render(request, 'cars/add.html'))

def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Cars.objects.get(pk=pk).delete()
            return (redirect('cars:list'))
        except:
            print("Error:  PK Not Found")
            return (redirect('cars:list'))
    else:
        return (render(request, 'cars/delete.html'))

def test(request):
    brand = request.session.get('brand')
    year = request.session.get('year')
    data = {'brand':brand, 'year':year}
    return (render(request, 'cars/test.html', {'data':data}))