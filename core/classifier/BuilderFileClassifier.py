from  core.validator.FileValidators import FileValidators

from core.classifier.TableFileClassifier import TableFileClassifier
from core.classifier.SequenceFileClassifier import SequenceFileClassifier
from core.classifier.PackageFileClassifier import PackageFileClassifier
from core.classifier.ViewFileClassifier import ViewFileClassifier
from core.classifier.ConstraintFileClassifier import ConstraintFileClassifier
from core.classifier.DefaultFileClassifier import DefaultFileClassifier

class BuilderFileClassifier():

    def build(self):

        tableFileClassifier      = TableFileClassifier()
        sequenceFileClassifier   = SequenceFileClassifier()
        tableFileClassifier.setNext(sequenceFileClassifier)
        packageFileClassifier    = PackageFileClassifier()
        sequenceFileClassifier.setNext(packageFileClassifier)


        vistaFileClassifier      = ViewFileClassifier()
        packageFileClassifier.setNext(vistaFileClassifier)

        constraintFileClassifier = ConstraintFileClassifier()
        vistaFileClassifier.setNext(constraintFileClassifier)


        defaultFileClassifier = DefaultFileClassifier()
        constraintFileClassifier.setNext(defaultFileClassifier)


        return tableFileClassifier
