# coding=utf-8
from  core.validator.FileValidator import FileValidator
from  core.validator.FileValidators import FileValidators

class SequenceFileValidator(FileValidator):

    def __init__(self):
        FileValidator.__init__(self)
        self.next = FileValidator()

    def setNext(self,next):
        print("next from sequence")
        self.next = next

    def isSecuence(self,file):
        expression = '[a-zA-Z][a-zA-Z][S]+_'
        return self.checkExpression(expression,file)


    def validate(self, file ):
        result =  self.isSecuence(file)
        if result:
            return FileValidators.SEQUENCE.value
        else:
            return self.next.validate(file)
