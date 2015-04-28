# coding=utf-8


from  core.validator.TableFileValidator import TableFileValidator
from  core.validator.SequenceFileValidator import SequenceFileValidator
<<<<<<< Updated upstream
from  core.validator.PackageFileValidator import PackageFileValidator
=======
from  core.validator.VistaFileValidator import VistaFileValidator
from  core.validator.ConstraintFileValidator import ConstraintFileValidator
>>>>>>> Stashed changes

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
        vistaValidator=VistaFileValidator()
        vistaValidator.setNext(packageValidator)
        constraintValidator=ConstraintFileValidator()
        constraintValidator.setNext(vistaValidator)

        return tableValidator
