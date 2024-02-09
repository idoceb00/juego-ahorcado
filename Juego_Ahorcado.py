from random import choice


def pide_letra():
    # Pedirle al usuario que escoja una letra
    return input("\n¿Escoge una letra?: ")


def letra_is_valid(letra):
    # Comprobar letra valida
    letra = list(letra)

    if len(letra) > 1:
        print("ERROR. Formato NO válido. Debe ser un único Carácter")
        return False
    else:
        return True


def letra_is_correct(letra, secret_word):
    # Comprobar letra correcta
    if letra.lower() in secret_word.lower():
        return True
    else:
        return False


def is_win(secret_word, letras_correctas):
    # Comprueba si ha ganado o no

    for letra in secret_word.lower():
        if letra not in letras_correctas:
            return False
        else:
            pass

    return True


def mostrar(secret_word, letras_correctas):
    word = ""
    for letra in secret_word:
        if letra.lower() in letras_correctas:
            word += letra
        else:
            word += "-"

    return word


# FLUJO PRINCIPAL DE EJECUCIÓN
dictionary_variado = (
"Ordenador", "Tablet", "Bolsa de Valores", "Cargador", "Elecciones", "Voto", "Mochila", "Persiana",
"Camiseta", "Reloj", "Vodka", "Calculadora", "Paraguas", "Pasamontañas", "Flexo", "Freixo",
"Aguacate", "Silla", "Altavoz", "Abogado", "Profesor", "Conserje", "Director", "Silla de ruedas",
"Masaje", "Comprensión lectora", "Amor propio", "Narcisismo", "Libreta", "Goma de borrar", "Zapatilla",
"Cerveza", "Vino", "Galicia",)

dictionary_galicia = ("A Coruña", "Sillobre", "Fene", "Ferrol", "Pontevedra", "Vigo", "Ourense", "Fisterra", "Cee",
                      "Ribeira", "Cambados", "Vilagarcía de Arousa", "Camariñas")

secret_word = choice(dictionary_variado)
letras_correctas = []
letras_incorrectas = []
vidas = 6
fin = 1

print("JUEGO DEL AHORCADO: ")
print(f"Bienvenido al juego del ahorcado!\nDebes adivinar la siguiente palabra secreta\n"
      f"y tienes un máximo de {vidas} errores posibles\nTu palabra secreta es:\n")

while fin == 1:
    # print(secret_word)
    print(mostrar(secret_word, letras_correctas) + f"\nVIDAS: {vidas}\nLetras incorrectas: {letras_incorrectas}")

    letra = pide_letra()

    if letra_is_valid(letra):
        if letra_is_correct(letra, secret_word):
            if letra.lower() not in letras_correctas:
                letras_correctas += letra.lower()
        else:
            if letra.lower() not in letras_incorrectas:
                letras_incorrectas += letra.lower()

            vidas -= 1

    if is_win(secret_word, letras_correctas):
        print(f"\n¡¡HAS GANADO!!\nLa palabra secreta era: {secret_word}")
        fin = 0
    elif vidas == 0:
        print(f"\nVIDAS: {vidas}\nGAME OVER\n\nSecret Word: {secret_word}")
        fin = 0

    print()
