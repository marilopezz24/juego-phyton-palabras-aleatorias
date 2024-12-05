#Juego realizado por Mariacarmen López López
# TOP SECRET ANIMALS

import random #importo random

# Lista de palabras de 5 letras
lista_palabras = ["araña", "abeja", "burro", "cabra", "cebra", "cerdo", "cisne", "erizo", "koala", "gallo", "tigre", "mosca", "monos", "morsa", "perro", "lince", "pulpo", "panda", "raton", "zorro"]

#Mensaje de bienvenida
print("BIENVENIDO A TOPSECRET ANIMALS")
#Instrucción para el jugador 
print("¿Consigues  adivinar el animal?")
  # Muestra la lista de palabras disponibles
print(f"{lista_palabras}")

# Selección aleatoria de una palabra
palabra = random.choice(lista_palabras)

#Añado pista, dando la primera letra
print("Te doy una pista inicial : " + palabra[0]) 

#Si pierdes 
ganar = False
# Informa sobre los intentos disponibles
print("Tienes 5 intentos")
#Intentos
for i in range(1,6): # (5 intentos)
    intento = input("Dime una palabra:")#Pide al jugador que ingrese una palabra
    # Si el jugador acierta
    if intento == palabra:
        ganar=True # Cambia la variable a True si  gana
        break #terminan los intentos
    else:
        print (f" Te quedan {5-i} intentos ") # Informa cuántos intentos quedan

#cuando acierta
if ganar==True: 
    # Si el jugador ganó
    print("¡Has ganado!")  # Muestra mensaje si pierde
else:
    print(" ¡Has perdido!")  # Muestra mensaje si gana

print(f"La palabra correcta era {palabra}.") #Finalmente muestra la palabra