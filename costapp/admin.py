from django.contrib import admin
from costapp.models import MyCost, AddIncome, CostName



admin.site.register(CostName)

admin.site.register(MyCost)
admin.site.register(AddIncome)

