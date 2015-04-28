# coding=utf-8

from  core.validator.FileValidator import FileValidator
from  core.validator.FileValidators import FileValidators


class DefaultFileValidator(FileValidator):

    def __init__(self):
        FileValidator.__init__(self)
        self.next = FileValidator()

    def setNext(self,next):
        self.next = next

    def isTable(self,file):
        expression = '[a-zA-Z][a-zA-Z][tT]+_([a-zA-Z])*.(sql|SQL)$'
        return self.checkExpression(expression,file)

    def validate(self, file ):
        return FileValidators.NO_VALID.value
