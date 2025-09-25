from datetime import datetime
import random

sensores = []

for i in range(5):
    temp = round(random.uniform(18, 32), 2)   
    humedad = round(random.uniform(30, 60), 2)  

    
    sensores.append((temp, datetime.now().strftime("%H:%M:%S"), "temperatura"))
    sensores.append((humedad, datetime.now().strftime("%H:%M:%S"), "humedad"))

print("\nLecturas de sensores:")
for lectura in sensores:
    print(lectura)

temperaturas = [valor for (valor, _, tipo) in sensores if tipo == "temperatura"]
promedio_temp = sum(temperaturas) / len(temperaturas)

print(f"\nPromedio de temperatura: {promedio_temp:.2f}°C")
