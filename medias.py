from random import choice

def cargaDatos(colores):
    medias=[]
    cantidad=int(input("ingrese cantidad de medias"))
    
    for i in range(cantidad):
        medias.append(choice(gama))
        
    return medias


def separarColores(medias,gama):
    pares=0
    
    for color in gama:
        veces=medias.count(color)
        
        if veces % 2==1:
            veces=veces-1
        
        pares=pares+veces/2
                                
    return pares


def imprimeResultado(medias,pares):
    
    print(medias)
    print("la cantidad de pares es "+ str(pares))

gama=["blanco","azul","verde"]
medias=cargaDatos(gama)
pares=separarColores(medias,gama)
imprimeResultado(medias, pares)

