from django.contrib import admin
from .models import storeStatusModel, menuHoursModel
# Register your models here.
admin.site.register(storeStatusModel)
admin.site.register(menuHoursModel)