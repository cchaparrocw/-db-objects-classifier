# coding=utf-8
from  core.validator.FileValidator import FileValidator
from  core.validator.FileValidators import FileValidators

class ConstraintFileValidator(FileValidator):

    def __init__(self):
        FileValidator.__init__(self)
        self.next = FileValidator()

    def setNext(self,next):
        self.next = next

    def isFk(self,file):
        expression = '[a-zA-Z][a-zA-Z][tT].*((_F[0-9]*)\.(sql))$'
        return self.checkExpression(expression,file)

    def isNoFk(self,file):
        expression = '[a-zA-Z][a-zA-Z][T]+_.*(_PK.SQL)$'
        return self.checkExpression(expression,file)

    def isUnique(self,file):
        expression = '[a-zA-Z][a-zA-Z][T]+_.*(_U[0-9]*.SQL)$'
        return self.checkExpression(expression,file)

    def validate(self, file ):
        if self.isFk(file):
            return FileValidators.CONSTRAINT_FK.value
        elif self.isUnique(file) | self.isNoFk(file):
            return FileValidators.CONSTRAINT_NOFK.value
        else :
           return self.next.validate(file)
