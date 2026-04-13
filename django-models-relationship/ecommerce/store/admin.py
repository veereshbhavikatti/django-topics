from django.contrib import admin
from .models import customer,Address,catrgory,product,order
# Register your models here.
admin.site.register(customer)
admin.site.register(Address)
admin.site.register(catrgory)
admin.site.register(product)
admin.site.register(order)