# coding=utf-8
import re
from core.validator.FileValidators import FileValidators
from core.validator.read.ReadingValidator import ReadingValidator


class TablesReadingValidator(ReadingValidator):

    def __init__(self):
        self.next = ReadingValidator()

    def setNext(self,next):
        self.next = next

    def isTable( self, path ):
        lines = open(path).readlines()
        lines = ''.join([line for line in lines])
        return True if "CREATE TABLE" in lines else False

    def validate(self,pathFile):
        if self.isTable(pathFile):
            return FileValidators.TABLE.value
        else:
            return self.next.validate(pathFile)
