
# coding=utf-8
"""
Script para organizar la información de la base de datos generada
De acuerdo a los estandares de casewaresa
"""

import os
import shutil
import re

def checkExpression( expression,value):
    """
    Funcion que verifica que un patron(expresion)
    conicida con en un valor.

    Parameters
    ----------
    expression:string
        Expresión regular a validar
    value:string
        Valor al que se le va verificar la expresion regular
    """
    value = value.upper()
    result = re.match( expression,value )
    return True if result else False


def esVistaJoin():
    expression = '[a-zA-Z][a-zA-Z][J]+_'
    return checkExpression(expression,archivo)


def esReporte():
    expression = '[a-zA-Z][a-zA-Z][R]+_'
    return checkExpression(expression,archivo)

def esBI():
    expression = '[a-zA-Z][a-zA-Z][B]+_'
    return checkExpression(expression,archivo)




print(esVistaDatos('LD_acumulado'))
