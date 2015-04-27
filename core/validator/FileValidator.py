
class FileValidator:

    def checkExpression( self,expression,value):
        """
        Funcion que verifica que un patron(expresion)
        conicida con en un valor.

        Parameters
        ----------
        expression:string
            Expresión regular a validar
        value:string
            Valor al que se le va verificar la expresion regular
        """
        value = value.upper()
        result = re.match( expression,value )
        return True if result else False

    def setNext(self,next):
        self.next = next

    def validate():
        pass
