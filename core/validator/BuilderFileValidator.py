# coding=utf-8


from  core.validator.TableFileValidator import TableFileValidator
from  core.validator.SequenceFileValidator import SequenceFileValidator
from  core.validator.PackageFileValidator import PackageFileValidator

class BuilderFileValidator:

    def build(self):
        """
        Funcion que verifica que tipo de archivo es
        Vista, secuencia,tabla
        """

        tableValidator = TableFileValidator()
        sequenceValidator = SequenceFileValidator()
        tableValidator.setNext(sequenceValidator)
        packageValidator = PackageFileValidator()
        packageValidator.setNext(sequenceValidator )

        return tableValidator
