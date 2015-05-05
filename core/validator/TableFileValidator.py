# coding=utf-8

from  core.validator.FileValidator import FileValidator
from  core.validator.FileValidators import FileValidators


class TableFileValidator(FileValidator):

    def __init__(self):
        FileValidator.__init__(self)
        self.next = FileValidator()

    def setNext(self,next):
        self.next = next

    def isTable(self,file):
        expression = '([a-zA-Z][a-zA-Z][tT]_(?:(?!F[0-9]|CONSTRAINT|U[0-9]|PK|REFCONSTRAINT|I[0-9]|B[0-9]|C[0-9]).)*?\.(sql|SQL))'
        return self.checkExpression(expression,file)

    def validate(self, file ):
        result =  self.isTable(file)
        if result:
            return FileValidators.TABLE.value
        else:
            return self.next.validate(file)
