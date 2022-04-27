 import numpy as np

def promedio(array):
    suma = 0
    for i in array:
        suma += i

    suma /= len(array)
    return suma


def desv_estandar(array, prom):
    suma = 0
    for i in array:
        suma += (i - prom)**2

    suma /= len(array)
    suma = suma**0.5
    return suma


def x_estandar(array, prom, desv):
    x = []
    for i in array:
        a = (i - prom)/desv
        x.append(a)

    return(x)


def estandarizacion(tabla):
    for t in tabla:
        i = t[0]
        print("\n\nVector: ", i)
        prom = promedio(i)
        desv = desv_estandar(i, prom)
        xEst = x_estandar(i, prom, desv)

        print("Promedio:    ", prom)
        print("Desviacion:  ", desv)
        print("X Estandar:  ", xEst)

