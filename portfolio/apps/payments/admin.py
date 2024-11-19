from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'servicio', 'fec_pago', 'pagado', 'prim_venc', 'seg_venc', 'importe')
    search_fields = ('servicio',)
    list_per_page = 20
    date_hierarchy = 'fec_pago'