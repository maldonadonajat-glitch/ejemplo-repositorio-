nombre = input("Ingresa el nombre de animal en plural")
archivo = open("mi_archivo.txt", "a")
archivo.write(f"tres tristes {nombre} \n")
archivo.close()
