sexo=input("[H]:hombre/[M]: Mujer").upper()
edad=int(input("Dame tu edad"))

if sexo[0]=="H" and edad>65:
    print("te jubilaras")
elif sexo[0]=="M" and edad>60:
    print("te jubilaras")
else: 
    print("aun no te toca")