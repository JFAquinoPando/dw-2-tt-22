"""
Leer dos números, si son iguales que se multipliquen, si el primero es mayor que el segundo que se resten y sino que se sumen
"""
numero1 = int(input("Ingrese un valor numérico: "))
numero2 = int(input("Ingrese un valor numérico: "))

if numero1 == numero2:
    res = numero1*numero2
    #print("El nro1:",numero1,"por nro2:",numero2, "=",numero1*numero2)
elif numero1 > numero2:
    res = numero1-numero2
    #print(numero1,"-",numero2,"=",numero1-numero2)
else:
    res = numero1+numero2
    #print(numero1,"+",numero2,"=",numero1+numero2)
print("El resultado es:", res)