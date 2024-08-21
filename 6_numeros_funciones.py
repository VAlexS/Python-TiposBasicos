import math


def get_potencia(base, exponente):
    return math.pow(base, exponente)

def get_raiz_cuadrada(numero):
    return math.sqrt(9)

#redondeo

print(round(1.3)) #imprime 1

print(round(1.7)) #imprime 2

print(round(1.5)) #imprime 2

#valor absoluto

print(abs(-77)) #imprime 77

print(abs(55)) #imprime 55

#ceil

print(math.ceil(1.1)) #imprime 2, ya que devuelve al superior entero más cerano

#floor

print(math.floor(1.999999999)) #imprime 1, ya que redondea al entero mas cercano, pero hacia abajo


#isann (is not an number)

if math.isnan(23):
    print("No es un numero")
else:
    print("Es un numero")

#potencia

potencia = get_potencia(2, 3)

print(potencia) #imprime 8

#raiz cuadrada

raiz_cuadrada = get_raiz_cuadrada(9)

print(raiz_cuadrada)
















