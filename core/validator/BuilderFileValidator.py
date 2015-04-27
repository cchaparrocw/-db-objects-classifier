class BuilderFileValidator:

    def getTypeFile(self):
        """
        Funcion que verifica que tipo de archivo es
        Vista, secuencia,tabla
        """
        vistaValidator = VistaValidator()
        tableValidator = TableValidator()
        vistaValidator.setNext(tableValidator)
        sequenceValidator = SequenceValidator()
        sequenceValidator.setNext(sequenceValidator)
