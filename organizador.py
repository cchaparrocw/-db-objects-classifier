
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

def esVistaDatos( archivo ):
    """
     Función que se encarga de validar si un archivo
     es una vista de datos.

     Parameters
     ----------
     archivo : string
         nombre del archivo que se va a verificar `x`.
    """
    #[a-zA-Z]: expresion que me dice que verifque
    #si es una letra en minúscula o en mayúscula.
    expression = '[a-zA-Z][a-zA-Z][D]+_'
    return checkExpression(expression,archivo)

def esVistaJoin():
    expression = '[a-zA-Z][a-zA-Z][J]+_'
    return checkExpression(expression,archivo)
def esLov():
    expression = '[a-zA-Z][a-zA-Z][L]+_'
    return checkExpression(expression,archivo)

def esReporte():
    expression = '[a-zA-Z][a-zA-Z][R]+_'
    return checkExpression(expression,archivo)

def esBI():
    expression = '[a-zA-Z][a-zA-Z][B]+_'
    return checkExpression(expression,archivo)

def inicializar():
    #verifico si existe la estructura creada anteriormente
    #para eliminarla
    #esto si se quiere borrar todo
    if os.path.exists( pathDeploy ):
        shutil.rmtree( pathDeploy )
    #creo la estructura de directorios para copiar la información
    #posteriormente.
    for path in paths:
        os.makedirs( pathDeploy + path )

pathDeploy = r'build/'
paths = [
    'sql/fisica/table',
    'sql/fisica/sequence',
    'sql/fisica/index',
    'sql/fisica/constraint',
    'sql/fisica/constraint/fk',
    'sql/fisica/constraint/nofk',
    'sql/fisica/logica-plsql',
    'sql/fisica/logica-plsql/package',
    'sql/fisica/logica-plsql/package-body',
    'sql/fisica/logica-plsql/trigger',
    'sql/query/datos',
    'sql/query/lov',
    'sql/query/join',
    'sql/query/report',
    'sql/query/bi'
]

print(esVistaDatos('LD_acumulado'))
