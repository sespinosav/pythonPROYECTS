"""

Enunciado

El gerente del aeropuerto internacional El Dorado desea hacer estadísticas sobre los vuelos en tres aerolíneas diferentes de acuerdo a dos modelos de aviones. Dichas estadísticas se efectuarán teniendo en cuenta la cantidad de pasajeros en cada uno de los aviones por una semana completa (lunes a domingo).

Cada avión posee la siguiente información:
ID del avión: “Avión ” + consecutivo que inicia en 1
Modelo: Puede ser Boeing 737 o Airbus A319
Aerolínea: Puede ser Avianca, Copa o Lan
Cantidad de pasajeros por día (CPD: en total 7): Entre 50 y 124

Elabore un algoritmo que permita calcular y mostrar en pantalla lo siguiente:

Generar aleatoriamente la información de cada avión (N en total), de acuerdo a los rangos dados en el enunciado. Dicha información deberá ser almacenada toda en arreglos. El ID del avión, Modelo y Aerolínea se almacenarán en una matriz de cadenas de caracteres. La cantidad de pasajeros por día por avión se almacenarán en una matriz numérica. Realice una función que genere los números aleatorios. Muestre todos los datos asociados a los aviones. Recuerde que por ningún motivo deberán ser ingresados los datos de forma manual.
Calcular cuál es el total de pasajeros diarios (7 en total). Almacenarlos y mostrarlos ya sea en un vector o en una fila adicional de la matriz.
Calcular y mostrar cuál es el promedio de pasajeros por aerolínea (son 3 promedios). Cree la función promedio para calcular y devolver dichos valores.
Calcular y mostrar cuál fue el día y a qué aerolínea y avión correspondió la mayor movilidad de pasajeros, es decir, encontrar el máximo valor de la matriz CPD y mostrar este valor además de sus datos asociados: Día de la semana, Aerolínea, ID del avión.
Ordene y muestre de forma descendente toda la información de los aviones de acuerdo al total de pasajeros diarios (calculado en el punto 2). No olvide que debe mostrar todos los datos: ID del avión, Modelo, Aerolínea, matriz CPD y Total de pasajeros diarios.

"""
#Importamos la libreria random
import random

#Inicializamos la matriz

matriz = [["ID", "MODELO", "AEROLINEA", "CANTIDAD DE PASAJEROS"]]

"""
La estructura de la matriz estará dada de la siguiente manera:

[ID,Modelo,Aerolinea,Cantidad de pasajeros]
[id_,modelo,aerolinea,[lunes,martes,miercoles,jueves,viernes,sabado,domingo]]
[id_,modelo,aerolinea,[lunes,martes,miercoles,jueves,viernes,sabado,domingo]]
[id_,modelo,aerolinea,[lunes,martes,miercoles,jueves,viernes,sabado,domingo]]
[id_,modelo,aerolinea,[lunes,martes,miercoles,jueves,viernes,sabado,domingo]]
[id_,modelo,aerolinea,[lunes,martes,miercoles,jueves,viernes,sabado,domingo]]

Para acceder a la cantidad de personas de un dia especifico haríamos lo siguiente

por ejemplo para el primer avion, la cantidad de pasajeros para el miercoles sería

matriz[1][3][2]

ya que los aviones empiezan en la segunda linea, y el indice de la segunda linea es 1
tomamos la posicion de ese arreglo que contiene los valores de la cantidad de pasajeros que esta en la 3
y para el dia miercoles se encuentra en la posicion 2

"""
#Creamos arreglos que contienen los valores que puede adquirir las columnas de la matriz

modelos_posibles = ["Boeing 737", "AirbusA319"]
aerolineas_posibles = ["Avianca", "Copa", "Lan"]

#PRIMER PUNTO

#Generamos la matriz aleatoriamente

#Pedimos la cantidad de vuelos

n = int(input("Ingrese el numero de vuelos: ")) #int() es un metodo que convierte la cadena de caracteres ingresado a numero

#Recorremos un for n veces mientras llenamos los datos a la vez en la matriz aleotriamente

for indice in range(n):
    id_ = "Avión" + str(indice+1) #convertimos el indice del avion a cadena de caracteres y luego lo sumamos con avión
    """
    Para tomar modelos y aerolineas aleatorias
    generamos un numero entre el limite inferior del indice del arreglo,
    que siempre es cero y el limite superior que depende de la cantidad de datos
    ese numeor es la cantidad de posibilidades - 1

    así por ejemplo si tenemos que
    modelos_posibles = ["Boeing 737", "AirbusA319"]
    hay dos posiblidades coger "Boeing 737" que esta en la posicion 0
    o coiger "AirbusA319" que esta en la posicion 1

    por lo tanto usamos random.randint(0,1)

    y en el caso de
    aerolineas_posibles = ["Avianca", "Copa", "Lan"]
    hay 3 posiciones, la 0, 1 y 2

    entonces random.randint(0,2)
    """
    modelo = modelos_posibles[random.randint(0,1)] #Tomamos una posicion aleatoria en modelos_posibles
    aerolinea = aerolineas_posibles[random.randint(0,2)] #Tomamos una posicion aleatoria en aerolineas_posibles

    #inicializamos el arreglo que contiene los valores de los dias

    cantidad_pasajeros = []

    #generamos la cantidad de pasajeros por dia

    for dia in range(7):
        cantidad_pasajeros.append(random.randint(50,124))

    datos_avion = [id_,modelo,aerolinea,cantidad_pasajeros] #Agregamos los valores a un arreglo
    matriz.append(datos_avion) #Agregamos los datos a la matriz

#Imprimimos la matriz

for renglon in matriz:
    print(renglon)

#PUNTO 2

print()

#Inicializamos el arreglo

cantidad_por_dias = [0,0,0,0,0,0,0]

#Calculamos la cantidad de pasajeros por día

for arreglo_dias in matriz:
    if "ID" not in arreglo_dias: #Nos aseguramos que no tomemos la primera linea de la matriz
        datos = arreglo_dias[3] #Cogemos el arreglo con la cantidas de dias

        """
        recorremos un ciclo 7 veces para
        obtrner los indices de los dias
        y luego le sumamos a la cantidad de
        pasajeros por dia la cantidad por dias
        en cada avion
        """

        for dia in range(7):
            cantidad_por_dias[dia] += datos[dia]

#Imprimimos la cantidad de pasajeros por dia

print("Cantidad de pasajeros totales el dia Lunes: ",cantidad_por_dias[0])

print("Cantidad de pasajeros totales el dia Martes: ",cantidad_por_dias[1])

print("Cantidad de pasajeros totales el dia Miercoles: ",cantidad_por_dias[2])

print("Cantidad de pasajeros totales el dia Jueves: ",cantidad_por_dias[3])

print("Cantidad de pasajeros totales el dia Viernes: ",cantidad_por_dias[4])

print("Cantidad de pasajeros totales el dia Sabados: ",cantidad_por_dias[5])

print("Cantidad de pasajeros totales el dias Domingos: ",cantidad_por_dias[6])

#PUNTO 3

print()

#Creamos la funcion promedio

def promedio(aerolinea):
    cantidad = 0 #Cantidad de aviones de la aerolinea
    suma = 0 #Suma total
    for avion in matriz:
        if "ID" not in avion and aerolinea not in avion:
            """
            Verificamos si no estamos en la primeara linea
            verificamos que la linea contenga la aerolinea que estamos evaluando
            """
            for pasajeros in avion[3]:
                cantidad += 1
                suma += pasajeros

    return suma/cantidad #promedio

#Imprimimos el promedio por aerolinea

for aerolinea in aerolineas_posibles:
    print("Promedio de pasajeros por dia en la aerolinea " + aerolinea + ": " + str(promedio(aerolinea)))

#PUNTO 4

print()

valor = 0 #Mayor valor encontrado
avion = 0 #Arreglo del avion que contiene al mayor valor
dia = 0 #Numero del dia de la semana

for linea in matriz:
    if "ID" not in linea: #Nos aseguramos que no tomemos la primera linea de la matriz

        contador = 0
        for pasajeros in linea[3]:
            if pasajeros > valor: #Evaluamos si este numero de pasajeros es mayor al valor mayor actual
                avion = linea
                valor = pasajeros
                dia = contador

            contador += 1

#Segun el valor del dia determinamos el dia en forma de cadena de caracteres

if dia == 0:
    dia_aux = "Lunes"
elif dia == 1:
    dia_aux = "Martes"
elif dia == 2:
    dia_aux = "Miercoles"
elif dia == 3:
    dia_aux = "Jueves"
elif dia == 4:
    dia_aux = "Viernes"
elif dia == 5:
    dia_aux = "Sabado"
else:
    dia_aux = "Domingo"

print("El dia mas transcurrido fue un " + dia_aux + " con " + str(valor) + " pasajeros " + " en la aerolinea "+ avion[2] + " con id de la avion " + avion[0])

#PUNTO 5

print()

ordenamiento = [avion] #Agregamos el avion con el numero mayor al ordenamiento

while(len(ordenamiento) < n):#Recorremos la matriz hasta que el ordenamiento se acabe

    mayor = 0

    avion = []

    for linea in matriz:
        if "ID" not in linea and linea not in ordenamiento: #Nos aseguramos que no tomemos la primera linea de la matriz ni un avion que ya haya sido organizado
             for pasajeros in linea[3]:
                if pasajeros > mayor:
                    mayor = pasajeros
                    avion = linea

    ordenamiento.append(avion)

print("Orden descendente por cantidad de pasajeros de los aviones en su dia mas transcurrente")

print()

for avion in ordenamiento:
    print(avion)
