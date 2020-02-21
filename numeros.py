def compruebaSiEsCentro(number):
    sumaAnteriores=sumaAntes(number)
    sumaPosteriores=sumaPost(number,sumaAnteriores)
        
    if sumaAnteriores==sumaPosteriores:
        print("encontrado!!!  " + str(number))
        return True
    else:
        return False


def sumaAntes(number):
    suma=0
    
    for i in range(number): 
        suma=suma+i
    
    return suma


def sumaPost(number,sumaAnteriores):
    number=number+1
    suma=number*2+1
    number=number+2
    
    while suma<sumaAnteriores:
        suma=suma+number
        number=number+1
    
    return suma


contador=0;
number=1

while contador<4:
    respuesta=compruebaSiEsCentro(number)
    
    if respuesta:        
        contador=contador+1
    
    number=number+1

