"""
2- 
Si el monto total de la compra excede de 500000:
    la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante.
Si el monto total de la compra no excede de 500000
    la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante.

El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.
"""
monto_total = int(input("Ingrese el monto total de la compra: "))
if monto_total > 500000:
    empresa = 55/100
    banco = 30/100
    credito = (100 - (empresa + banco))/100
else:
    empresa = 70/100
    credito = 30/100
    banco = 0/100

print("Empresa paga: ",empresa,"%:", monto_total * empresa)
print("Banco paga: ",banco,"%:", monto_total * banco)
print("Credito (sin recarga): ",credito,"%:", monto_total * credito)
print("Credito: (recarga 20%)",(credito * 1.2),"%:", monto_total * ((credito * 1.2)))
cuenta = (empresa + banco + (credito * 1.2))
a_pagar = monto_total * cuenta
print("Y pago?", a_pagar)