#encoding: UTF-8

# Autor: Marina Itzel Haro Hernndez, A01373471 
# Te da el precio dependiendo de cuantas peliculas normales y de estreno compraste

def calcularRenta(numeroEstrenos, numeroNormales) :
 # Calcula y guarda en la variable totalPago el total a pagar
    totalEstrenos = numeroEstrenos*45.00
    totalNormales = numeroNormales*27.00
    totalPago = totalEstrenos + totalNormales
 # Regresa totalPago
    return totalPago
 
def main() :
    #estrenos = Leer el número de pelculas de estreno
    numeroEstrenos = int(input("Peliculas de estreno"))
    #normales = Leer el número de pelculas normales
    numeroNormales = int(input("Peliculas normales"))
    #Calcula el resultado llamando a la función calcularRenta
    calcular = calcularRenta(numeroEstrenos, numeroNormales)
    #Imprimir los tres datos     
    print("Películas de estreno rentadas:", numeroEstrenos)
    print("Peliculas normales rentadas:", numeroNormales)
    print("Total a pagar: $%.2f" % (calcular))
    
main()