
def primera_aparicion(str, caracter):
    return str.find(caracter) #devuelve la posicion donde encuentra el caracter por primera vez, o -1 si no encuentra nada

def existe_caracter(str, caracter):
    return caracter in str


objeto = " cometa "

'''
print(objeto.strip().capitalize()) #El metodo capitalize transforma la primera letra a mayuscula si no hay espacios en blanco

print(objeto.title()) #aunque haya espacios en blanco, la primera letra la transforma a mayuscula
'''

print(objeto.lstrip())

print(objeto.rstrip())

#BUSQUEDAS EN STRINGS

frase = "Esta tarde me ire a volar la cometa"

posicion = primera_aparicion(frase, "j")

print(posicion)


frase = frase.replace("volar", "jugar con") #remplaza una cadena por otra que la pasamos como segundo argumento

print(frase) #imprime Esta tarde me ire a jugar con la cometa

existe = existe_caracter(frase, "v")

print(existe) #devuelve False

existe = existe_caracter(frase, "e")

print(existe) #devuelve True


#negacion

print("j" not in frase) #imprime false

