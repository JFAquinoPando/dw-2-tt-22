"""
Ingresar dos valores en las variables “maximo” y “minimo” y luego ingresar un valor en la variable “temperatura”. 
Imprime un mensaje si el valor de temperatura no está dentro del rango de marcado por minimo y maximo
"""
maximo = int(input("Ingresa un valor maximo: "))
minimo = int(input("Ingresa un valor minimo: "))
temperatura = int(input("Ingresa un valor para la temperatura: "))

if (temperatura >= minimo and temperatura <= maximo):
    print("Esta dentro del rango!")
else:
    print("Esta fuera del rango!")