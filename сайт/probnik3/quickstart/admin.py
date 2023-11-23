from django.contrib import admin
from quickstart.models import BankClients, BankWorkers, InvestType, MoneyCourse, InvestRegist

# Register your models here.

admin.site.register(InvestType)
admin.site.register(BankClients)
admin.site.register(BankWorkers)
admin.site.register(MoneyCourse)
admin.site.register(InvestRegist)
