# Calcula el minimo de movimientos para resolver la torre de hanoi usando la formula 2^n-1

def calcular_minimo_teorico(num_discos: int) -> int:
    if num_discos < 1:
        raise ValueError("El número de discos debe ser al menos 1")
    return (2**num_discos) - 1

# Diccionario de configuración
# NIVELES 1 AL 5

CONFIGURACION_NIVELES = {
    1: {
        "nombre": "Nivel 1 - Tutorial (Modo libre)",
        "num_discos": 3,
        "limite_movimientos": None,  # Ilimitado
        "descripcion": "Aprende las reglas básicas sin presión de movimientos",
    },
    2: {
        "nombre": "Nivel 2 - Básico",
        "num_discos": 4,
        "limite_movimientos": 20,  # Minimo 15 con +5 de margen
        "descripcion": "Empieza el verdadero reto con límite estricto de movimientos",
    },
    3: {
        "nombre": "Nivel 3 - Intermedio",
        "num_discos": 5,
        "limite_movimientos": 38,  # Minimo 31 con +7 de margen
        "descripcion": "Requiere planificación. Límite ajustado",
    },
    4: {
        "nombre": "Nivel 4 - Avanzado",
        "num_discos": 6,
        "limite_movimientos": 72,  # Minimo 63 con +9 de margen
        "descripcion": "Pocos errores permitidos. Límite ajustado",
    },
    5: {
        "nombre": "Nivel 5 - Maestro Hanói",
        "num_discos": 7,
        "limite_movimientos": 140,  # Minimo 127 +13 de margen
        "descripcion": "El desafío final con margen mínimo"
    }
}

# Devuelve toda la información necesaria para iniciar un nivel
def obtener_datos_nivel(nivel: int) -> dict:
    if nivel not in CONFIGURACION_NIVELES:
        raise ValueError(f"El nivel {nivel} no existe")

    datos = CONFIGURACION_NIVELES[nivel].copy()
    datos["minimo_teorico"] = calcular_minimo_teorico(datos["num_discos"])
    return datos

# Devuelve el numero del siguiente nivel si aun quedan niveles
def obtener_siguiente_nivel(nivel_actual: int):
    siguiente = nivel_actual + 1
    if siguiente in CONFIGURACION_NIVELES:
        return siguiente
    return None

# Retorna la cantidad de niveles disponibles
def obtener_total_niveles() -> int:
    return len(CONFIGURACION_NIVELES)

# Bloque de prueba individual e integracion con motor_juego.py
if __name__ == "__main__":
    import motor_juego

    nivel = 1
    while nivel is not None:
        datos = obtener_datos_nivel(nivel)
        juego = motor_juego.JuegoHanoi(
            num_discos=datos["num_discos"],
            limite_movimientos=datos["limite_movimientos"]
        )
        print(
            f"{datos['nombre']} | Discos: {juego.num_discos} | "
            f"Mínimo teórico: {datos['minimo_teorico']} | "
            f"Límite: {juego.movimientos_restantes}"
        )
        nivel = obtener_siguiente_nivel(nivel)
    print("Juego finalizado")