import random 

temp = round (random.uniform(10,40),2);

print(f"Lectura de temperatura: {temp} °C");

if 18<= temp <=30: 
    print ("La temperatura esta en rango seguro.")
else: 
    print ("Alerta: Temperatura esta fuera de rango.")