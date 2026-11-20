# Controla las reglas estrictas de la Torre de Hanoi, validaciones y estado de victoria/derrota.

import pila

class JuegoHanoi:
    # Inicializa las 3 torres, carga los discos en la primera y configura los limites
    def __init__(self, num_discos, limite_movimientos=None):
        self.num_discos = num_discos
        self.movimientos_realizados = 0
        self.movimientos_restantes = limite_movimientos  # Si es None, el nivel tiene paso libre
        
        # Creamos las 3 torres usando los modulo utilizados en clase
        self.torres = {
            "1": pila.crear_pila(),  # Torre Origen
            "2": pila.crear_pila(),  # Torre Auxiliar
            "3": pila.crear_pila()   # Torre Destino
        }
        
        # Llenamos la torre 1 (origen) de mayor a menor (ej. 3 abajo, 2 en medio, 1 arriba)
        for disco in range(num_discos, 0, -1):
            pila.push(self.torres["1"], disco)

    # Valida y ejecuta el movimiento de un disco entre dos torres
    def mover_disco(self, origen, destino):
        # 1. Validar que las torres ingresadas existan ("1", "2" o "3")
        if origen not in self.torres or destino not in self.torres:
            return False, "Error: Debes elegir torres validas (1, 2 o 3)."
            
        if origen == destino:
            return False, "Movimiento invalido: La torre de origen y destino son la misma."

        torre_origen = self.torres[origen]
        torre_destino = self.torres[destino]

        # 2. Validar que la torre de origen no este vacia
        if pila.is_empty(torre_origen):
            return False, f"Movimiento invalido: La torre {origen} esta vacia."

        # 3. Mirar los discos superiores sin sacarlos (usando peek)
        disco_a_mover = pila.peek(torre_origen)
        disco_destino = pila.peek(torre_destino)

        # 4. Regla estricta: No colocar un disco grande sobre uno mas pequeño
        if disco_destino is not None and disco_a_mover > disco_destino:
            return False, f"Movimiento invalido: No puedes poner el disco {disco_a_mover} sobre el disco {disco_destino}."

        # 5. Si pasa todas las validaciones, ejecutamos el movimiento (pop y push)
        disco = pila.pop(torre_origen)
        pila.push(torre_destino, disco)
        
        # Actualizamos contadores
        self.movimientos_realizados += 1
        if self.movimientos_restantes is not None:
            self.movimientos_restantes -= 1

        return True, f"Disco {disco} movido de la torre {origen} a la {destino}."

    # Revisa si todos los discos llegaron a la torre 3 (Destino)
    def verificar_victoria(self):
        return pila.size(self.torres["3"]) == self.num_discos

    # Revisa si se agotaron los movimientos (aplica del Nivel 2 en adelante)
    def verificar_derrota(self):
        if self.movimientos_restantes is None:
            return False  # En Nivel 1 (paso libre) nunca pierdes por movimientos
        return self.movimientos_restantes <= 0 and not self.verificar_victoria()

    # Reinicia el tablero al estado inicial del nivel
    def reiniciar_partida(self, limite_movimientos=None):
        self.__init__(self.num_discos, limite_movimientos)


# Bloque de prueba individual (para comprobar que las reglas funcionan antes de unir todo)
if __name__ == "__main__":
    juego = JuegoHanoi(num_discos=3, limite_movimientos=10)
    print("Torres iniciales:", juego.torres)
    
    # Prueba 1: Movimiento valido (mover disco 1 de torre 1 a torre 3)
    exito, mensaje = juego.mover_disco("1", "3")
    print(mensaje)
    
    # Prueba 2: Movimiento invalido (intentar poner disco 2 sobre disco 1)
    exito, mensaje = juego.mover_disco("1", "3")
    print(mensaje)
    
    print("Torres despues de pruebas:", juego.torres)
    print("Movimientos restantes:", juego.movimientos_restantes)