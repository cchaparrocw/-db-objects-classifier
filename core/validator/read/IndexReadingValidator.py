# coding=utf-8
import re
from core.validator.FileValidators import FileValidators
from core.validator.read.ReadingValidator import ReadingValidator


class IndexReadingValidator(ReadingValidator):

    def __init__(self):
        self.next = ReadingValidator()

    def setNext(self,next):
        self.next = next

    def isIndex( self, pathIndex ):
        lines = open(pathIndex).readlines()
        lines = ''.join([line for line in lines])
        return True if "INDEX" in lines else False

    def validate(self,pathFile):
        if self.isIndex(pathFile):
            print("soy indice")
            return FileValidators.INDEX.value
        else:
            return self.next.validate(pathFile)
