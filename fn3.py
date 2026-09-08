# Función para calcular el impuesto según el tipo de producto
def calcular_monto_impuesto(monto, tipo):
    if tipo == 1:
        porcentaje = 18  # IGV / IVA estándar
    elif tipo == 2:
        porcentaje = 10  # Impuesto reducido
    elif tipo == 3:
        porcentaje = 0   # Exonerado
    else:
        porcentaje = -1  # Tipo inválido
        
    if porcentaje == -1:
        return -1
    else:
        return (monto * porcentaje) / 100

# Programa Principal (Menú)
continuar = "si"

print("========================================")
print("  BIENVENIDO A LA CALCULADORA DE IMPUESTOS  ")
print("========================================")

while continuar == "si" or continuar == "s":
    # 1. Ingreso de datos
    monto_base = float(input("\nIngrese el monto base: $"))
    
    print("\nTipos de producto:")
    print("1. General (18%)")
    print("2. Reducido (10%)")
    print("3. Alimentos/Medicina (0%)")
    tipo_producto = int(input("Seleccione el tipo (1, 2 o 3): "))
    
    # 2. Proceso (Llamada a la función)
    impuesto = calcular_monto_impuesto(monto_base, tipo_producto)
    
    # 3. Salida de resultados
    if impuesto == -1:
        print("\n[ERROR] Opción de tipo de producto incorrecta.")
    else:
        total = monto_base + impuesto
        print("\n--------- RESULTADOS ---------")
        print(f"Monto Base:  ${monto_base:.2f}")
        print(f"Impuesto:    ${impuesto:.2f}")
        print(f"Total Neto:  ${total:.2f}")
        print("------------------------------")
        
    # Preguntar si desea hacer otro cálculo
    continuar = input("\n¿Desea calcular otro impuesto? (si/no): ").lower()

print("\n¡Gracias por usar el programa! Éxitos en tu proyecto.")