# Proyecto-Parcial-3-Torre-de-Han-i
Aplicación interactiva y funcional del clásico rompecabezas matemático **Torre de Hanói**, desarrollada en **Python** como proyecto parcial para la asignatura **Manejo y Estructura de Datos** de la carrera de Ingeniería en Desarrollo de Software.

---

## Equipo de Desarrollo y Distribución de Roles

El proyecto ha sido desarrollado de forma modular por un equipo de 5 integrantes, integrando estructuras de datos avanzadas, lógica de validación, algoritmos de soporte y una interfaz interactiva de alta calidad:

| Integrante | Rol Principal | Módulos y Responsabilidades Asignadas |
| :--- | :--- | :--- |
| **Integrante 1** | **Estructuras de Datos Base** | • Modelado de torres mediante **pilas (LIFO)** implementadas con listas en Python.<br>• Uso de **tuplas** para configuraciones inmutables (límites de discos y parámetros estáticos).<br>• Gestión del estado global mediante un **diccionario** dinámico (`origen`, `auxiliar`, `destino`). |
| **Integrante 2** | **Lógica de Juego y Reglas** | • Desarrollo de **funciones** de movimiento y validación de reglas (prohibido colocar un disco mayor sobre uno menor).<br>• Cálculo matemático dinámico del mínimo teórico de movimientos ($2^n - 1$) mediante **operaciones** aritméticas.<br>• Control de bucles de partida y contadores. |
| **Integrante 3** | **Historial y Algoritmo de Soporte** | • Implementación de un registro histórico de jugadas utilizando una **cola (FIFO)**.<br>• Desarrollo de un módulo opcional de resolución automática basado en **árboles de búsqueda / grafos de estados** para mostrar la ruta óptima. |
| **Integrante 4** | **Interfaz de Usuario (UI) - Parte 1** | • Diseño de la experiencia visual interactiva (interfaz gráfica o consola enriquecida con formato ASCII/ANSI).<br>• Programación de menús de inicio, selección de cantidad de discos en rango configurable y renderizado visual. |
| **Integrante 5** | **Interfaz de Usuario (UI) - Parte 2 & QA** | • Conexión de eventos de la **interfaz de usuario** con las funciones de lógica y validación.<br>• Diseño de pantallas secundarias (mensajes de victoria, alertas de errores, botón de reinicio).<br>• Coordinación de pruebas funcionales y redacción del documento técnico. |

---

## Requerimientos Técnicos y Conceptos Aplicados

- **Lenguaje:** Python (versión 3.x recomendada).
- **Estructuras de Datos:** 
  - **Pilas (LIFO):** Para representar el apilamiento de discos en cada torre.
  - **Colas (FIFO):** Para el registro de historial de movimientos.
  - **Diccionarios y Tuplas:** Para la gestión de estados y configuraciones inmutables.
  - **Grafos / Árboles de Búsqueda:** Para el análisis de estados y resolución automática.
- **Paradigma:** Programación modular y orientada a objetos según diseño seleccionado.

---

## Reglas del Juego Implementadas

1. **Tres Torres:** El juego cuenta con una torre de *Origen*, una *Auxiliar* y un *Destino*.
2. **Orden Inicial:** Los discos comienzan ordenados de mayor a menor (de abajo hacia arriba) en la torre de origen.
3. **Movimiento Único:** Solo se puede mover un disco a la vez.
4. **Disco Superior:** Únicamente es posible mover el disco que se encuentra en la parte superior de cualquier torre.
5. **Restricción de Tamaño:** Ningún disco grande puede ser colocado sobre un disco más pequeño.
6. **Detección de Victoria:** El software identifica automáticamente cuando todos los discos se han trasladado con éxito a la torre de destino.
7. **Validación de Entradas:** Los movimientos inválidos son rechazados inmediatamente con un mensaje explicativo claro para el usuario.

---

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone "https://github.com/tu-usuario/torre-hanoi-edatos.git"
