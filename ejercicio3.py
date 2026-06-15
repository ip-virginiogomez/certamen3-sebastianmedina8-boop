edad = int(input("ingrese su edad: "))
tarjeta = input("Tiene tarjeta de socio s/n: ")
total = int(input("ingresa el total de su compra: "))

if edad >= 60 and (tarjeta == "s" or total >= '10000' ):
    print("Si obtiene el 15%  :D")
    descuento = total*0.15
    total_d = total-descuento
    print("Su monto a pagar es:", total_d)
else:
    print("No cumple los requisitos :c")
