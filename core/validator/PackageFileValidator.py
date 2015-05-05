# coding=utf-8

from  core.validator.FileValidator import FileValidator
from  core.validator.FileValidators import FileValidators


class PackageFileValidator(FileValidator):

    def __init__(self):
        FileValidator.__init__(self)
        self.next = FileValidator()

    def setNext(self,next):
        self.next = next

    def isPackage(self,file):
        expressionPackage = '[a-zA-Z][a-zA-Z][P]+_.*(.pks|.sql)$'
        return self.checkExpression(expressionPackage,file)

    def isPackageBody(self,file):
        expressionPackage = '[a-zA-Z][a-zA-Z][P]+_.*(.pkb|._1.sql)$'
        return self.checkExpression(expressionPackage,file)

    def validate(self, file ):
        if self.isPackage(file):
            return FileValidators.PACKAGE.value
        elif self.isPackageBody(file):
            return FileValidators.PACKAGE_BODY.value
        else:
            return self.next.validate(file)
