# coding=utf-8

class VistaFileValidator(FileValidator):

    def __init__(self):
        FileValidator.__init__(self)

    def isJoin(self,file):
        expression = '[a-zA-Z][a-zA-Z][J]+_'
        return checkExpression(expression,file)

    def isLov(self,file):
        expression = '[a-zA-Z][a-zA-Z][L]+_'
        return checkExpression(expression,file)

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
        expression = '[a-zA-Z][a-zA-Z][D]+_'
        return checkExpression(expression,file)
