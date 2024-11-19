from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['servicio', 'fec_pago', 'prim_venc', 'seg_venc', 'importe', 'pagado']
        widgets = {
            'fec_pago': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
            'prim_venc': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
            'seg_venc': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
            'pagado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'fec_pago': 'Fecha de Pago',
        }