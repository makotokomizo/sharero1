from django.contrib import admin
from .models import Plan, Transaction, ConnectAccount, Customer
# Register your models here.

admin.site.register(Plan)
admin.site.register(Transaction)
admin.site.register(ConnectAccount)
admin.site.register(Customer)


