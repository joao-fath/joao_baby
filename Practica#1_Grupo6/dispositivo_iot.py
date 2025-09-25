import random
from datetime import datetime

# Simular lecturas de sensores
temperatura = round(random.uniform(20, 35), 2)   # grados °C
humedad = round(random.uniform(20, 60), 2)       # porcentaje %
hora_actual = datetime.now().hour                # hora del sistema

print(f"Temperatura: {temperatura}°C")
print(f"Humedad: {humedad}%")
print(f"Hora actual: {hora_actual}:00")

# Control de dispositivos con estructuras de control
if temperatura > 28:
    print("Activando ventilador...")
else:
    print("Ventilador apagado.")

if humedad < 40:
    print("Activando humidificador...")
else:
    print("Humidificador apagado.")

if hora_actual >= 18:
    print("Encendiendo luces...")
else:
    print("Luces apagadas.")
