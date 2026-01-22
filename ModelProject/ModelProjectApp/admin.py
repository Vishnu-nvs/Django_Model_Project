from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=['name','Cust_Id','email','date_of_join','salary']
    search_fields=['name','email']
    list_filter=['date_of_join','salary']
admin.site.register(Customer,CustomerAdmin)
