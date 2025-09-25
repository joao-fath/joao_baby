# -*- coding: utf-8 -*-
"""
ANALIZADOR DE DATOS DE SENSORES - PROGRAMA 5
Procesa lecturas de sensores y detecta valores atípicos
Paleta de colores morada: #4B0082, #800080, #9370DB, #D8BFD8
"""

import math
import statistics
from datetime import datetime

class AnalizadorSensores:
    def __init__(self):
        """Inicializa el analizador de datos de sensores"""
        self.datos_sensores = []  # Lista de tuplas (valor, tipo, timestamp)
        self.colores = {
            'titulo': '\033[95m',      # Morado claro
            'normal': '\033[0m',       # Reset color
            'estadistica': '\033[94m', # Azul morado
            'atipico': '\033[91m',     # Rojo para atípicos
            'normal_val': '\033[92m',  # Verde para normales
            'advertencia': '\033[93m', # Amarillo
            'dato': '\033[96m'         # Cian
        }
    
    def agregar_lectura(self, valor: float, tipo_sensor: str, timestamp: str = None):
        """
        Agrega una lectura de sensor al analizador
        
        Args:
            valor (float): Valor de la lectura
            tipo_sensor (str): Tipo de sensor
            timestamp (str): Marca de tiempo (opcional)
        """
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        lectura = (valor, tipo_sensor, timestamp)
        self.datos_sensores.append(lectura)
        
        print(f"{self.colores['dato']}✓ Lectura agregada: {valor} ({tipo_sensor}){self.colores['normal']}")
    
    def filtrar_por_tipo(self, tipo_sensor: str):
        """
        Filtra lecturas por tipo de sensor
        
        Args:
            tipo_sensor (str): Tipo de sensor a filtrar
        """
        return [d for d in self.datos_sensores if d[1] == tipo_sensor]
    
    def calcular_estadisticas(self, tipo_sensor: str = None):
        """
        Calcula estadísticas básicas para los datos
        
        Args:
            tipo_sensor (str): Tipo de sensor específico (opcional)
        """
        datos = self.datos_sensores if tipo_sensor is None else self.filtrar_por_tipo(tipo_sensor)
        
        if not datos:
            return {}
        
        valores = [d[0] for d in datos]
        
        # Cálculo de estadísticas básicas
        estadisticas = {
            "maximo": max(valores),
            "minimo": min(valores),
            "promedio": statistics.mean(valores),
            "mediana": statistics.median(valores),
            "desviacion_estandar": statistics.stdev(valores) if len(valores) > 1 else 0,
            "rango": max(valores) - min(valores),
            "cantidad": len(valores)
        }
        
        return estadisticas
    
    def detectar_valores_atipicos(self, tipo_sensor: str = None):
        """
        Detecta valores atípicos usando el método del rango intercuartílico
        
        Args:
            tipo_sensor (str): Tipo de sensor específico (opcional)
        """
        datos = self.datos_sensores if tipo_sensor is None else self.filtrar_por_tipo(tipo_sensor)
        
        if len(datos) < 3:
            return []  # No se pueden detectar atípicos con pocos datos
        
        valores = [d[0] for d in datos]
        
        # Calcular cuartiles
        q1 = statistics.quantiles(valores, n=4)[0]  # Primer cuartil (25%)
        q3 = statistics.quantiles(valores, n=4)[2]  # Tercer cuartil (75%)
        iqr = q3 - q1  # Rango intercuartílico
        
        # Definir límites para valores atípicos
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        
        # Identificar valores atípicos
        atipicos = []
        for dato in datos:
            valor = dato[0]
            if valor < limite_inferior or valor > limite_superior:
                atipicos.append({
                    "valor": valor,
                    "tipo_sensor": dato[1],
                    "timestamp": dato[2],
                    "desviacion": abs(valor - statistics.mean(valores))
                })
        
        return atipicos
    
    def verificar_umbrales_seguros(self, tipo_sensor: str):
        """
        Verifica si las lecturas están dentro de umbrales seguros
        
        Args:
            tipo_sensor (str): Tipo de sensor a verificar
        """
        datos = self.filtrar_por_tipo(tipo_sensor)
        
        if not datos:
            return []
        
        valores = [d[0] for d in datos]
        
        # Definir umbrales seguros según el tipo de sensor
        umbrales = {
            "temperatura": {"min": 18.0, "max": 30.0},
            "humedad": {"min": 30.0, "max": 80.0},
            "presion": {"min": 1000.0, "max": 1020.0},
            "calidad_aire": {"min": 0.0, "max": 100.0}
        }
        
        if tipo_sensor not in umbrales:
            return []
        
        min_seguro = umbrales[tipo_sensor]["min"]
        max_seguro = umbrales[tipo_sensor]["max"]
        
        # Encontrar valores fuera de umbral seguro
        fuera_umbral = []
        for dato in datos:
            valor = dato[0]
            if valor < min_seguro or valor > max_seguro:
                fuera_umbral.append({
                    "valor": valor,
                    "timestamp": dato[2],
                    "estado": "BAJO" if valor < min_seguro else "ALTO"
                })
        
        return fuera_umbral
    
    def generar_reporte_completo(self):
        """
        Genera un reporte completo con todas las estadísticas
        """
        print(f"\n{self.colores['titulo']}{'='*80}")
        print("                     REPORTE COMPLETO DE SENSORES")
        print(f"{'='*80}{self.colores['normal']}")
        
        # Obtener todos los tipos de sensores únicos
        tipos_sensores = list(set(d[1] for d in self.datos_sensores))
        
        for tipo in tipos_sensores:
            datos_tipo = self.filtrar_por_tipo(tipo)
            
            if not datos_tipo:
                continue
            
            print(f"\n{self.colores['estadistica']}📊 {tipo.upper()}:{self.colores['normal']}")
            
            # Calcular estadísticas
            stats = self.calcular_estadisticas(tipo)
            print(f"   • Lecturas: {stats['cantidad']}")
            print(f"   • Rango: {stats['minimo']:.2f} - {stats['maximo']:.2f}")
            print(f"   • Promedio: {stats['promedio']:.2f}")
            print(f"   • Desviación estándar: {stats['desviacion_estandar']:.2f}")
            
            # Detectar valores atípicos
            atipicos = self.detectar_valores_atipicos(tipo)
            if atipicos:
                print(f"   {self.colores['atipico']}• Valores atípicos: {len(atipicos)}{self.colores['normal']}")
                for atipico in atipicos[:3]:  # Mostrar solo los 3 primeros
                    print(f"     ◦ {atipico['valor']:.2f} (desviación: {atipico['desviacion']:.2f})")
            
            # Verificar umbrales seguros
            if tipo in ["temperatura", "humedad"]:
                fuera_umbral = self.verificar_umbrales_seguros(tipo)
                if fuera_umbral:
                    print(f"   {self.colores['advertencia']}• Valores fuera de umbral seguro: {len(fuera_umbral)}{self.colores['normal']}")

# Función principal del programa 5
def ejecutar_analizador_sensores():
    """Ejecuta el analizador de datos de sensores"""
    analizador = AnalizadorSensores()
    
    print(f"{analizador.colores['titulo']}📊 INICIANDO ANALIZADOR DE DATOS DE SENSORES{analizador.colores['normal']}")
    
    # Generar datos de ejemplo más realistas con algunos valores atípicos
    print(f"\n{analizador.colores['dato']}📝 GENERANDO DATOS DE EJEMPLO...{analizador.colores['normal']}")
    
    # Datos normales de temperatura (20°C ± 3°C)
    for i in range(20):
        valor = 20.0 + (random.uniform(-3, 3))
        analizador.agregar_lectura(round(valor, 1), "temperatura", f"2023-10-15 {10+i//2}:{i%2*30:02d}")
    
    # Algunos valores atípicos de temperatura
    analizador.agregar_lectura(35.5, "temperatura", "2023-10-15 11:45")  # Muy alto
    analizador.agregar_lectura(12.3, "temperatura", "2023-10-15 12:15")  # Muy bajo
    
    # Datos de humedad (50% ± 15%)
    for i in range(15):
        valor = 50.0 + (random.uniform(-15, 15))
        analizador.agregar_lectura(round(valor, 1), "humedad", f"2023-10-15 {11+i//3}:{i%3*20:02d}")
    
    # Algunos valores atípicos de humedad
    analizador.agregar_lectura(85.7, "humedad", "2023-10-15 12:30")  # Muy alto
    analizador.agregar_lectura(25.2, "humedad", "2023-10-15 13:10")  # Muy bajo
    
    # Datos de presión (1010 ± 5)
    for i in range(10):
        valor = 1010.0 + (random.uniform(-5, 5))
        analizador.agregar_lectura(round(valor, 1), "presion", f"2023-10-15 {12+i//2}:{i%2*30:02d}")
    
    # Generar reporte completo
    analizador.generar_reporte_completo()
    
    # Análisis específico por tipo de sensor
    print(f"\n{analizador.colores['titulo']}🔍 ANÁLISIS DETALLADO POR SENSOR:{analizador.colores['normal']}")
    
    for tipo in ["temperatura", "humedad", "presion"]:
        datos = analizador.filtrar_por_tipo(tipo)
        if datos:
            print(f"\n{analizador.colores['estadistica']}📈 {tipo.upper()}:{analizador.colores['normal']}")
            stats = analizador.calcular_estadisticas(tipo)
            print(f"   • Mínimo: {stats['minimo']:.2f}")
            print(f"   • Máximo: {stats['maximo']:.2f}")
            print(f"   • Promedio: {stats['promedio']:.2f}")
            
            atipicos = analizador.detectar_valores_atipicos(tipo)
            print(f"   • Valores atípicos: {len(atipicos)}")
            
            if tipo in ["temperatura", "humedad"]:
                fuera_umbral = analizador.verificar_umbrales_seguros(tipo)
                print(f"   • Fuera de umbral seguro: {len(fuera_umbral)}")

if __name__ == "__main__":
    import random  # Importar aquí para no afectar el resto del código
    ejecutar_analizador_sensores()