# coding=utf-8
from  core.validator.FileValidator import FileValidator
from  core.validator.FileValidators import FileValidators

class VistaFileValidator(FileValidator):

    def __init__(self):
        FileValidator.__init__(self)
        self.next = FileValidator()

    def setNext(self,next):
        self.next = next

    def isJoin(self,file):
        expression = '[a-zA-Z][a-zA-Z][jJ]+_'
        return self.checkExpression(expression,file)

    def isBI(self,file):
        expression = '[a-zA-Z][a-zA-Z][bB]+_'
        return self.checkExpression(expression,file)

    def isReport(self,file):
        expression = '[a-zA-Z][a-zA-Z][rR]+_'
        return self.checkExpression(expression,file)

    def isLov(self,file):
        expression = '[a-zA-Z][a-zA-Z][lL]+_'
        return self.checkExpression(expression,file)

    def isData( self,file ):
        """
         Función que se encarga de validar si un archivo
         es una vista de datos.

         Parameters
         ----------
         archivo : string
             nombre del archivo que se va a verificar `x`.
        """
        #[a-zA-Z]: expresion que me dice que verifque
        #si es una letra en minúscula o en mayúscula.
        expression = '[a-zA-Z][a-zA-Z][dD]+_'
        return self.checkExpression(expression,file)

    def validate(self, file ):
        if self.isData(file):
            return FileValidators.VIEW_DATA.value
        elif self.isJoin(file):
            return FileValidators.VIEW_JOIN.value
        elif self.isLov(file):
            return FileValidators.VIEW_LOV.value
        elif self.isReport(file):
            return FileValidators.VIEW_REPORT.value
        elif self.isBI(file):
            return FileValidators.VIEW_BI.value
        else :
            return self.next.validate(file)
