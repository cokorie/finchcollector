from django.contrib import admin
from .models import Feeding, Finch

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)