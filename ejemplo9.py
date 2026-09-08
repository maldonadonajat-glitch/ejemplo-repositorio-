import keyboard
import time

# Abrimos el archivo en modo 'a' (append) para añadir texto sin borrar el contenido
archivo = open("mi_archivo.txt", "a")

print("Escribe los nombres de animales. Presiona la tecla 'ESC' en cualquier momento para salir.\n")

while True:
    # 1. Verifica si se presionó la tecla Escape
    if keyboard.is_pressed('esc'):
        print("\n¡Tecla 'Esc' detectada. Deteniendo el bucle!")
        break

    # 2. Tu lógica para solicitar e insertar en el archivo
    nombre = input("Ingresa el nombre de animal en plural (o presiona Enter): ")
    
    if nombre.strip():  # Solo escribe si el usuario no dejó la línea vacía
        archivo.write(f"tres tristes {nombre} \n")
        print(f"-> Guardado: tres tristes {nombre}")

    time.sleep(0.1)

# 3. Cierra el archivo al salir del bucle
archivo.close()