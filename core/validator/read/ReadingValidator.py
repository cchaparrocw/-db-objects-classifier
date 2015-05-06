# coding=utf-8
import re


class ReadingValidator:

    def __init__(self):
        pass
    def setNext(self,next):
         raise NotImplementedError('subclasses must override setNext()!')

    def validate(self,pathFile):
        """
        Función que se encarga de validar que tipo de archivo es.

        Parameters
        ----------
        file:string
            Nombre del archivo a validar.
        """
        raise NotImplementedError('subclasses must override validate()!')
