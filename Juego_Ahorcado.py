from random import choice


def pide_letra():
    # Pedirle al usuario que escoja una letra
    return input("¿Escoge una letra?: ")


def letra_is_valid(letra):
    # Comprobar letra valida
    if type(letra) is not str:
        return False
    else:
        return True


def letra_is_correct(letra, secret_word):
    # Comprobar letra correcta
    if letra is secret_word:
        return True
    else:
        return False


def is_win(secret_word, word, vidas):
    # Comprueba si ha ganado o no

    for sw_char, w_char in zip(secret_word, word):
        if (sw_char != w_char) and vidas == 0:
            return False
        else:
            pass

    return True


def mostrar(secret_word, vidas, letras_correctas):
    word = ""
    for letra in secret_word:
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

print("JUEGO DEL AHORCADO: ")
print(f"Bienvenido al juego del ahorcado!\nDebes adivinar la siguiente palabra secreta\n"
      f"y tienes un máximo de {vidas} errores posibles\nTu palabra secreta es:\n")




