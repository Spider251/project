from django.shortcuts import render
from .models import *


# Create your views here.
def Upimg(request):
    if request.method == 'POST':
        new_brand = Brand()
        new_brand.logo = request.FILES.get('picc')
        new_brand.title = 'BMW'
        new_brand.newprice = 11.11
        new_brand.save()
        return render(request, 'upimg.html')
    if request.method == 'GET':
        return render(request, 'upimg.html')
