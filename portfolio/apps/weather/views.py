from django.shortcuts import render
import requests
from datetime import datetime, timedelta

# Vista para mostrar el clima
def get_weather(request):
    city = request.GET.get('city', 'Buenos Aires')
    api_key = '3e8bcb91d14bb1cd1563ac6574679433'
    # Consultamos los 40 próximos pronósticos (para cubrir 7 días)
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt=40&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    forecast = []
    if response.status_code == 200:
        # Para los 7 días de la semana (lunes a domingo)
        current_day = datetime.utcnow().weekday()  # Día actual de la semana (0 = lunes, 6 = domingo)
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        # Usamos un índice para recorrer los 7 días
        forecast_days = {day: None for day in days_of_week}
        
        for item in data['list']:
            # Convertimos la fecha a un objeto datetime
            dt = datetime.utcfromtimestamp(item['dt'])
            # Obtenemos el nombre del día
            day_name = dt.strftime('%A')

            # Filtramos los datos por los próximos 7 días
            if day_name in forecast_days and forecast_days[day_name] is None:
                # Obtenemos la descripción del clima (soleado, nublado, lluvia, etc.)
                weather_condition = item['weather'][0]['main']
                forecast_days[day_name] = {
                    'day': day_name,
                    'temperature': item['main']['temp'],
                    'weather_condition': weather_condition
                }
        
        # Ahora aseguramos que la lista `forecast` tenga los 7 días
        for day in days_of_week:
            if forecast_days[day]:
                forecast.append(forecast_days[day])

    return render(request, 'weather.html', {'forecast': forecast, 'city': city})
