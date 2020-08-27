# Ejercicio 16
# https://j2logo.com/ejercicios/ejercicio-16-cuenta-subcadenas/

def cuenta_subcadenas_ax(cadena):
    respuesta = 0
    if cadena.startswith('A'):
        respuesta = cadena.count('X') + cuenta_subcadenas_ax(cadena[1:])
    elif len(cadena) > 1:
        respuesta = cuenta_subcadenas_ax(cadena[1:])
    return respuesta
