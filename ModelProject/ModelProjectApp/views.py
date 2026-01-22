from django.shortcuts import render
from .models import Customer
# Create your views here.


def Customer_Details(request):
    cust=Customer.objects.all()
    return render(request,'Customer.html',{'data':cust})
