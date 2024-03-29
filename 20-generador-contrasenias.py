import random


def generar_contrasenia():
    mayusculas = ['A',  'B',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'J', 'K',
                  'L',  'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
                '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasenia = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasenia.append(caracter_random)
    contrasenia = ''.join(contrasenia)
    return contrasenia


def run():
    contrasenia = generar_contrasenia()
    print("Tu nueva contraseña es ", contrasenia)


if __name__ == "__main__":
    run()
