

import argparse
from ast import parse
from email import parser
import numpy as np

def calcular_valores_cetrales(lista_numero):
    media = np.mean(lista_numero)
    desv_std= np.std(lista_numero)
    return media,desv_std

def calcular_suma(lista_numero):
    resultado = np.sum(lista_numero)
    return resultado
def calcular_valores(lista_numero):
    """calcula LA SUMA"""
    suma=calcular_suma(lista_numero)
    return suma
def main():
    parser= argparse.ArgumentParser()
    parse.pa
    lista_numero=[1,5,8,45,9,23]
    suma= calcular_valores(lista_numero)
    print(suma)
    
    if __name__ == "__main__":
        main()
