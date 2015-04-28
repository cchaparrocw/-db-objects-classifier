# coding=utf-8


from  core.validator.TableFileValidator import TableFileValidator
from  core.validator.SequenceFileValidator import SequenceFileValidator
from  core.validator.PackageFileValidator import PackageFileValidator
from  core.validator.VistaFileValidator import VistaFileValidator
from  core.validator.ConstraintFileValidator import ConstraintFileValidator
from  core.validator.DefaultFileValidator import DefaultFileValidator


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
        sequenceValidator.setNext(packageValidator )

        vistaValidator=VistaFileValidator()
        packageValidator.setNext(vistaValidator)

        constraintValidator=ConstraintFileValidator()
        vistaValidator.setNext(constraintValidator)
        constraintValidator.setNext(vistaValidator)

        defaultValidator = DefaultFileValidator()
        #apuntar el siguiente al ultimo
        constraintValidator.setNext(defaultValidator)
        return tableValidator
