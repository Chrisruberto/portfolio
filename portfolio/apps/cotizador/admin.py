from django.contrib import admin
from .models import Dolar

class DolarAdmin(admin.ModelAdmin):
     list_display = ['nombre','compra','venta','fecha_actualizacion']


admin.site.register(Dolar, DolarAdmin)