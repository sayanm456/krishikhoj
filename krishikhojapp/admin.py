from django.contrib import admin
from .models import Tractor, Farmer

# Register your models here.
admin.site.register(Tractor)
admin.site.register(Farmer)