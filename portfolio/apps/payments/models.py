from django.db import models

class Servicio(models.Model):
    servicio = models.CharField(max_length=100)
    fec_pago = models.DateField(null=True, blank=True)
    pagado = models.BooleanField(null=True, blank=True)
    prim_venc = models.DateField(null=True, blank=True, verbose_name='Primer Vencimiento')
    seg_venc = models.DateField(null=True, blank=True, verbose_name='Segundo Vencimiento')
    importe = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.servicio} - {self.importe}'