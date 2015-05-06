# coding=utf-8
from core.validator.FileValidators import FileValidators
from core.validator.read.ReadingValidator import ReadingValidator


class ConstraintReadingValidator(ReadingValidator):

    def __init__(self):
        self.next = ReadingValidator()

    def setNext(self,next):
        self.next = next

    def validate(self,path):
        lines = open(path).readlines()
        lines = ''.join([line for line in lines])
        constraintsNoFk = ["PRIMARY" ,"UNIQUE","CHECK" ]
        if "ALTER TABLE" in lines and "FOREIGN" in lines:
            return FileValidators.CONSTRAINT_FK.value
        elif "ALTER TABLE" in lines and ( True for nofk in constraintsNoFk  if nofk in lines):
            return FileValidators.CONSTRAINT_NOFK.value
        else:
            return self.next.validate(path) 
