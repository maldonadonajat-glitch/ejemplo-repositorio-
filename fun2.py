def saludo(nombre):
    for i in range(1,10):
        print(f"HOLA {nombre}")

def sumar(a,b):
    suma= a+b
    return suma

print("PROGRAMA PRINCIPAL")
name = input("y tu como te llamas????? ")
saludo("tony")

resultado = sumar(4,6)
print(f"RESULTADO: {resultado}")
print(f"otra suna 65 + 12 = {sumar(65,12)}")

