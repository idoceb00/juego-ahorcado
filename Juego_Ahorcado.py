from random import choice


def pide_letra():
    # Pedirle al usuario que escoja una letra
    return input("¿Escoge una letra?: ")


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
    for letra in secret_word.lower():
        if letra in letras_correctas:
            word += letra
        else:
            word += "-"

    return word


# FLUJO PRINCIPAL DE EJECUCIÓN
dictionary = ("Ordenador", "Portátil", "Tablet", "Bolsa de Valores", "Cargador", "Elecciones", "Voto", "Mochila"
              , "Persiana", "Camiseta", "Reloj")
secret_word = choice(dictionary)
letras_correctas = []
letras_incorrectas = []
vidas = 6
fin = 1

print("JUEGO DEL AHORCADO: ")
print(f"Bienvenido al juego del ahorcado!\nDebes adivinar la siguiente palabra secreta\n"
      f"y tienes un máximo de {vidas} errores posibles\nTu palabra secreta es:\n")

while fin == 1:
    print(secret_word)
    print(mostrar(secret_word, letras_correctas) + f"\nLetras incorrectas: {letras_incorrectas}\nVIDAS: {vidas}")

    letra = pide_letra()

    if letra_is_valid(letra):
        if letra_is_correct(letra, secret_word):
            letras_correctas += letra
        else:
            letras_incorrectas += letra
            vidas -= 1

    if is_win(secret_word, letras_correctas):
        print("Enhorabuena Has ganado")
        fin = 0
    elif vidas == 0:
        print("GAME OVER")
        fin = 0
