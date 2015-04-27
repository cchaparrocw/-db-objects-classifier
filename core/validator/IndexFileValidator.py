# coding=utf-8

from  core.validator.FileValidator import FileValidator
from  core.validator.FileValidators import FileValidators


class IndexFileValidator(FileValidator):

    def __init__(self):
        FileValidator.__init__(self)
        self.next = FileValidator()

    def setNext(self,next):
        self.next = next

    def isIndex(self,file):
        expressionPackage = '[a-zA-Z][a-zA-Z][T]+_.*((_i[0-9]*).sql)'
        return self.checkExpression(expressionPackage,file)

    def validate(self, file ):
        if self.isIndex(file):
            return FileValidators.INDEX.value
        else:
            return self.next.validate(file)
