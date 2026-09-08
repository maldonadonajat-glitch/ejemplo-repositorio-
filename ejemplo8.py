#Modificar para que en cada interaccion inserte una nueva linea en un archivo 
import time
import keyboard
archivo = open("mi_archivo.txt", "w")
linea=0
while True:
    print("😈 ***\n")
    archivo.write(f"{linea} ===> *******\n")
    linea += 1
    if keyboard.is_pressed("esc"):
        print("\nTecla ESC detectada. Deteniendo el bucle")
        archivo.close()
        break
    
    # Tu lógica dentro del bucle
    print("procesando..." , end="\r")
    time.sleep(0.1) 