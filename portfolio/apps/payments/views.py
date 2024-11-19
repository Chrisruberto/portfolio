from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio
from .forms import ServicioForm
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.utils.timezone import now
from datetime import timedelta

def create_pago(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pago_list')
    else:
        form = ServicioForm()
    return render(request, 'create_pago.html', {'form': form})

def pago_list(request):
    today = now()
    # Obtener el mes seleccionado de la URL, si no es válido, usar el mes actual
    try:
        selected_month = int(request.GET.get('month', today.month))  # Asegura que sea un entero
        if selected_month < 1 or selected_month > 12:
            selected_month = today.month  # Si el mes no es válido, usar el mes actual
    except ValueError:
        selected_month = today.month  # En caso de error, usar el mes actual

    # Filtrar los pagos por el mes seleccionado
    start_of_month = today.replace(month=selected_month, day=1)
    next_month = start_of_month + timedelta(days=32)
    start_of_next_month = next_month.replace(day=1)

    # Obtener todos los pagos que tienen el primer vencimiento en el mes seleccionado
    pagos = Servicio.objects.filter(
        prim_venc__gte=start_of_month,
        prim_venc__lt=start_of_next_month
    )
    
    # Calcular el total pagado en el mes seleccionado solo de pagos que están marcados como pagados
    total_pagado = pagos.filter(pagado=True).aggregate(total=Sum('importe'))['total'] or 0

    return render(request, 'pago_list.html', {
        'pagos': pagos,
        'selected_month': selected_month,
        'total_pagado': total_pagado,
    })

def edit_pago(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('pago_list')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'create_pago.html', {'form': form})

def delete_pago(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('pago_list')
    return render(request, 'confirm_delete.html', {'servicio': servicio})