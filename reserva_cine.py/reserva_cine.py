"""
SISTEMA DE RESERVA DE ASIENTOS - SALA DE CINE
Tarea Semana 12: Gestión de reservas mediante matriz 3x4
Autor: [Diana Salome Romero Reyes]
Universidad Estatal Amazónica
Objetivo: Crear matriz 3x4 para gestionar reservas e imprimir su estado con bucles anidados
"""

# 1. Crear la matriz de asientos: 3 filas, 4 columnas, todos libres (0)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# 2. Solicitar datos al usuario
print("=== SISTEMA DE RESERVA - SALA DE CINE ===")
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# 3. Validar rango y reservar el asiento: asignar 1 en la posición indicada
if 0 <= fila <= 2 and 0 <= columna <= 3:
    asientos[fila][columna] = 1
    print(f"\n✅ Reserva realizada: Fila {fila}, Columna {columna}")
else:
    print("\n❌ Error: Fila debe ser 0 a 2 | Columna debe ser 0 a 3")

# 4. Mostrar el estado completo de la sala en formato de tabla
print("\n=== ESTADO DE LA SALA ===")
print("0 = Libre  |  1 = Reservado")
for i in range(3):          # Recorre cada fila (índice i)
    for j in range(4):      # Recorre cada columna de la fila (índice j)
        print(asientos[i][j], end=" ")  # Imprime en la misma línea
    print()                  # Salto de línea al terminar cada fila
    
if asientos[fila][columna]== 0:
    asientos[fila][columna]= 1
    print(f"\n Reserva realizada:Fila{fila},Columna {columna}")
else:
    print(f"\n El asiento ya esta reservado")

    
