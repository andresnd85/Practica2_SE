# Practica2_SE
from tabulate import tabulate

# Inicializa la lista de animales
animales = [
    {"nombre": "León", "es_carnívoro": True, "tiene_melena": True, "vive_en_selva": True},
    {"nombre": "Delfín", "es_carnívoro": True, "tiene_melena": False, "vive_en_selva": False},
]

def mostrar_animales(animales):
    # Esta función muestra una tabla con los atributos de los animales
    # Utiliza la librería 'tabulate' para formatear los datos de manera legible
    headers = ["Nombre", "Es Carnívoro", "Tiene Melena", "Vive en Selva"]
    tabla = [[animal["nombre"], animal["es_carnívoro"], animal["tiene_melena"], animal["vive_en_selva"]] for animal in animales]
    print(tabulate(tabla, headers, tablefmt="grid"))

def adivinar_animal(animales):
    # Esta función realiza el juego de "Adivina Quién"
    # Hace preguntas al usuario y filtra la lista de animales en consecuencia
    for atributo in ["es_carnívoro", "tiene_melena", "vive_en_selva"]:
        respuesta = hacer_pregunta(f"¿El animal que estás pensando tiene '{atributo.replace('_', ' ')}'? (s/n): ")
        animales[:] = [animal for animal in animales if animal[atributo] == (respuesta == 's')]

def hacer_pregunta(pregunta):
    # Esta función toma una pregunta y espera una respuesta 's' o 'n' del usuario
    respuesta = input(pregunta).lower()
    while respuesta not in ['s', 'n']:
        print("Respuesta no válida. Por favor, responda con 's' o 'n'.")
        respuesta = input(pregunta).lower()
    return respuesta

def agregar_nuevo_animal():
    # Esta función permite al usuario agregar un nuevo animal a la lista
    nombre = input("Ingrese el nombre del nuevo animal: ")
    es_carnivoro = hacer_pregunta("¿Es carnívoro? (s/n): ") == 's'
    tiene_melena = hacer_pregunta("¿Tiene melena? (s/n): ") == 's'
    vive_en_selva = hacer_pregunta("¿Vive en la selva? (s/n): ") == 's'
    animales.append({"nombre": nombre, "es_carnívoro": es_carnivoro, "tiene_melena": tiene_melena, "vive_en_selva": vive_en_selva})

def agregar_atributo_individual(atributo):
    # Esta función permite al usuario agregar un nuevo atributo a cada animal en la lista
    valor = hacer_pregunta(f"¿Todos los animales tienen '{atributo.replace('_', ' ')}'? (s/n): ") == 's'
    for animal in animales:
        animal[atributo] = valor

def jugar_de_nuevo():
    # Esta función pregunta al usuario si desea jugar nuevamente
    return hacer_pregunta("¿Quieres jugar de nuevo? (s/n): ") == 's'

# El bucle principal del juego
while True:
    # Muestra la lista actual de animales
    mostrar_animales(animales)

    # Intenta adivinar el animal del usuario
    adivinar_animal(animales)

    # Pregunta si el usuario quiere jugar de nuevo
    if not jugar_de_nuevo():
        # Si no quiere jugar de nuevo, pregunta si quiere agregar un nuevo animal
        if hacer_pregunta("¿Quieres agregar un nuevo animal? (s/n): ") == 's':
            # Si sí, agrega el nuevo animal y pregunta si quiere agregar un nuevo atributo
            agregar_nuevo_animal()
            if hacer_pregunta("¿Quieres agregar un nuevo atributo? (s/n): ") == 's':
                nuevo_atributo = input("Nombre del nuevo atributo a agregar a cada animal: ")
                agregar_atributo_individual(nuevo_atributo)
        else:
            # Si no quiere agregar un nuevo animal, termina el juego
            print("¡Gracias por jugar! Hasta luego!")
            break
