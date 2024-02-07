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


# Comprueba si ha ganado o no