# -*- coding: utf-8 -*-
"""
SISTEMA DE REGISTRO DE DISPOSITIVOS IoT - PROGRAMA 4
Registra y gestiona dispositivos IoT usando diccionarios
Paleta de colores morada: #4B0082, #800080, #9370DB, #D8BFD8
"""

class RegistroDispositivosIoT:
    def __init__(self):
        """Inicializa el sistema de registro de dispositivos"""
        self.dispositivos = []  # Lista de diccionarios con dispositivos
        self.colores = {
            'titulo': '\033[95m',      # Morado claro
            'normal': '\033[0m',       # Reset color
            'activo': '\033[92m',      # Verde para activos
            'inactivo': '\033[91m',    # Rojo para inactivos
            'dato': '\033[94m',        # Azul morado
            'busqueda': '\033[93m',    # Amarillo
            'exito': '\033[96m'        # Cian
        }
    
    def agregar_dispositivo(self, id: str, tipo: str, ubicacion: str, 
                           estado: str = "activo", ultimo_mantenimiento: str = "N/A"):
        """
        Agrega un nuevo dispositivo al registro
        
        Args:
            id (str): ID único del dispositivo
            tipo (str): Tipo de dispositivo
            ubicacion (str): Ubicación del dispositivo
            estado (str): Estado (activo/inactivo)
            ultimo_mantenimiento (str): Fecha último mantenimiento
        """
        # Verificar que el ID no exista ya
        for dispositivo in self.dispositivos:
            if dispositivo["ID"] == id:
                print(f"{self.colores['inactivo']}❌ Error: El ID {id} ya existe{self.colores['normal']}")
                return False
        
        # Crear diccionario con los datos del dispositivo
        dispositivo = {
            "ID": id,
            "tipo": tipo,
            "ubicación": ubicacion,
            "estado": estado,
            "último_mantenimiento": ultimo_mantenimiento
        }
        
        # Agregar a la lista
        self.dispositivos.append(dispositivo)
        print(f"{self.colores['exito']}✅ Dispositivo {id} agregado correctamente{self.colores['normal']}")
        return True
    
    def buscar_por_ubicacion(self, ubicacion: str):
        """
        Busca dispositivos por ubicación
        
        Args:
            ubicacion (str): Ubicación a buscar
        """
        dispositivos_encontrados = []
        
        for dispositivo in self.dispositivos:
            # Buscar coincidencia exacta (case insensitive)
            if dispositivo["ubicación"].lower() == ubicacion.lower():
                dispositivos_encontrados.append(dispositivo)
        
        return dispositivos_encontrados
    
    def actualizar_estado(self, id_dispositivo: str, nuevo_estado: str):
        """
        Actualiza el estado de un dispositivo
        
        Args:
            id_dispositivo (str): ID del dispositivo
            nuevo_estado (str): Nuevo estado (activo/inactivo)
        """
        for dispositivo in self.dispositivos:
            if dispositivo["ID"] == id_dispositivo:
                # Verificar que el nuevo estado sea válido
                if nuevo_estado.lower() in ["activo", "inactivo"]:
                    dispositivo["estado"] = nuevo_estado.lower()
                    print(f"{self.colores['exito']}✅ Estado de {id_dispositivo} actualizado a {nuevo_estado}{self.colores['normal']}")
                    return True
                else:
                    print(f"{self.colores['inactivo']}❌ Error: Estado debe ser 'activo' o 'inactivo'{self.colores['normal']}")
                    return False
        
        print(f"{self.colores['inactivo']}❌ Error: Dispositivo {id_dispositivo} no encontrado{self.colores['normal']}")
        return False
    
    def actualizar_mantenimiento(self, id_dispositivo: str, fecha_mantenimiento: str):
        """
        Actualiza la fecha de último mantenimiento
        
        Args:
            id_dispositivo (str): ID del dispositivo
            fecha_mantenimiento (str): Fecha del mantenimiento
        """
        for dispositivo in self.dispositivos:
            if dispositivo["ID"] == id_dispositivo:
                dispositivo["último_mantenimiento"] = fecha_mantenimiento
                print(f"{self.colores['exito']}✅ Mantenimiento de {id_dispositivo} actualizado{self.colores['normal']}")
                return True
        
        print(f"{self.colores['inactivo']}❌ Error: Dispositivo {id_dispositivo} no encontrado{self.colores['normal']}")
        return False
    
    def mostrar_dispositivos(self, lista_dispositivos=None):
        """
        Muestra dispositivos en formato tabla
        
        Args:
            lista_dispositivos: Lista específica de dispositivos (opcional)
        """
        if lista_dispositivos is None:
            lista_dispositivos = self.dispositivos
        
        if not lista_dispositivos:
            print(f"{self.colores['dato']}📭 No hay dispositivos para mostrar{self.colores['normal']}")
            return
        
        print(f"\n{self.colores['titulo']}{'='*80}")
        print("                          DISPOSITIVOS REGISTRADOS")
        print(f"{'='*80}{self.colores['normal']}")
        
        print(f"{self.colores['dato']}{'ID':<10} {'TIPO':<20} {'UBICACIÓN':<15} {'ESTADO':<10} {'MANTENIMIENTO':<15}{self.colores['normal']}")
        print("-" * 80)
        
        for dispositivo in lista_dispositivos:
            estado_color = self.colores['activo'] if dispositivo["estado"] == "activo" else self.colores['inactivo']
            print(f"{dispositivo['ID']:<10} {dispositivo['tipo']:<20} {dispositivo['ubicación']:<15} "
                  f"{estado_color}{dispositivo['estado']:<10}{self.colores['normal']} {dispositivo['último_mantenimiento']:<15}")

# Función principal del programa 4
def ejecutar_registro_dispositivos():
    """Ejecuta el sistema de registro de dispositivos IoT"""
    sistema = RegistroDispositivosIoT()
    
    print(f"{sistema.colores['titulo']}🏢 INICIANDO SISTEMA DE REGISTRO DE DISPOSITIVOS IoT{sistema.colores['normal']}")
    
    # Agregar dispositivos de ejemplo
    dispositivos_ejemplo = [
        {"id": "SEN-001", "tipo": "sensor_temperatura", "ubicacion": "sala", "estado": "activo", "mantenimiento": "2023-10-01"},
        {"id": "SEN-002", "tipo": "sensor_humedad", "ubicacion": "cocina", "estado": "activo", "mantenimiento": "2023-09-15"},
        {"id": "ACT-001", "tipo": "ventilador", "ubicacion": "sala", "estado": "inactivo", "mantenimiento": "2023-08-20"},
        {"id": "ACT-002", "tipo": "humidificador", "ubicacion": "dormitorio", "estado": "inactivo", "mantenimiento": "2023-07-10"},
        {"id": "ACT-003", "tipo": "luz_inteligente", "ubicacion": "sala", "estado": "activo", "mantenimiento": "2023-06-05"},
        {"id": "SEN-003", "tipo": "sensor_presencia", "ubicacion": "entrada", "estado": "activo", "mantenimiento": "2023-05-12"}
    ]
    
    print(f"\n{sistema.colores['dato']}📦 AGREGANDO DISPOSITIVOS DE EJEMPLO...{sistema.colores['normal']}")
    for dispositivo in dispositivos_ejemplo:
        sistema.agregar_dispositivo(
            dispositivo["id"],
            dispositivo["tipo"],
            dispositivo["ubicacion"],
            dispositivo["estado"],
            dispositivo["mantenimiento"]
        )
    
    # Mostrar todos los dispositivos
    sistema.mostrar_dispositivos()
    
    # Buscar dispositivos por ubicación
    print(f"\n{sistema.colores['busqueda']}🔍 BUSCANDO DISPOSITIVOS EN 'SALA':{sistema.colores['normal']}")
    dispositivos_sala = sistema.buscar_por_ubicacion("sala")
    sistema.mostrar_dispositivos(dispositivos_sala)
    
    # Actualizar estados de dispositivos
    print(f"\n{sistema.colores['busqueda']}🔄 ACTUALIZANDO ESTADOS DE DISPOSITIVOS:{sistema.colores['normal']}")
    sistema.actualizar_estado("ACT-001", "activo")  # Activar ventilador
    sistema.actualizar_estado("SEN-002", "inactivo")  # Desactivar sensor
    
    # Actualizar mantenimiento
    sistema.actualizar_mantenimiento("ACT-003", "2023-10-15")
    
    # Intentar actualizar dispositivo inexistente
    sistema.actualizar_estado("DIS-999", "activo")
    
    # Mostrar estado final
    print(f"\n{sistema.colores['titulo']}📊 ESTADO FINAL DE DISPOSITIVOS:{sistema.colores['normal']}")
    sistema.mostrar_dispositivos()
    
    # Estadísticas finales
    print(f"\n{sistema.colores['exito']}📈 ESTADÍSTICAS DEL SISTEMA:{sistema.colores['normal']}")
    print(f"• Total dispositivos: {len(sistema.dispositivos)}")
    activos = sum(1 for d in sistema.dispositivos if d["estado"] == "activo")
    print(f"• Dispositivos activos: {activos}")
    print(f"• Dispositivos inactivos: {len(sistema.dispositivos) - activos}")

if __name__ == "__main__":
    ejecutar_registro_dispositivos()