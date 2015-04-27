# coding=utf-8
import re

class FileValidator:

    def __init__(self):
        pass
    def checkExpression( self,expression,value):
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

    def setNext(self,next):
         raise NotImplementedError('subclasses must override setNext()!')

    def validate(self,file):
        """
        Función que se encarga de validar que tipo de archivo es.

        Parameters
        ----------
        file:string
            Nombre del archivo a validar.
        """
        raise NotImplementedError('subclasses must override validate()!')
