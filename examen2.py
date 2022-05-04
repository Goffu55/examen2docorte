estacion=[
    [4,6],
    [6,5],
    [7,3],
    [4,5],
]

n=4

print("Ingrese Punto de Origen, Por ejemplo: s1, s2, s3, s4")
estacionInicial = input()



if estacionInicial == "s1":
    i=0
    while i < 4:
        resta = estacion[i][0] - estacion[i][1]
        i += 1
    print("El camion NO llega a su punto de origen")

if estacionInicial == "s2":
    i=0
    posicioninicial = 1
    while i < 4:
        if posicioninicial  == 4:
            posicioninicial = 0
            resta = estacion[posicioninicial][0] - estacion[posicioninicial][1]
        resta = estacion[posicioninicial][0] - estacion[posicioninicial][1]
        posicioninicial +=1
        i += 1
    print("El camion NO llega a su punto de origen")

if estacionInicial == "s3":
    i=0
    posicioninicial = 2
    while i < 4:
        if posicioninicial  == 4:
            posicioninicial = 0
            resta = estacion[posicioninicial][0] - estacion[posicioninicial][1]
        resta = estacion[posicioninicial][0] - estacion[posicioninicial][1]
        posicioninicial +=1
        i += 1
        print(resta)
    print("El camion SI llega a su punto de origen")

if estacionInicial == "s4":
    i=0
    posicioninicial = 3
    while i < 4:
        if posicioninicial  == 4:
            posicioninicial = 0
            resta = estacion[posicioninicial][0] - estacion[posicioninicial][1]
        resta = estacion[posicioninicial][0] - estacion[posicioninicial][1]
        posicioninicial +=1
        i += 1
        print(resta)
    print("El camion NO llega a su punto de origen")

