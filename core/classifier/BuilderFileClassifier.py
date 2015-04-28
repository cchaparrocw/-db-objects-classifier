from  core.validator.FileValidators import FileValidators

from core.classifier.TableFileClassifier import TableFileClassifier
from core.classifier.SequenceFileClassifier import SequenceFileClassifier
from core.classifier.PackageFileClassifier import PackageFileClassifier
from core.classifier.ViewFileClassifier import ViewFileClassifier
from core.classifier.ConstraintFileClassifier import ConstraintFileClassifier

class BuilderFileClassifier():

    def build(self):
        tableFileClassifier      = TableFileClassifier()
        sequenceFileClassifier   = SequenceFileClassifier()
        tableFileClassifier.setNext(sequenceFileClassifier)
        packageFileClassifier    = PackageFileClassifier()
        packageFileClassifier.setNext(sequenceFileClassifier)
        vistaFileClassifier      = ViewFileClassifier()
        vistaFileClassifier.setNext(packageFileClassifier)
        constraintFileClassifier = ConstraintFileClassifier()
        constraintFileClassifier.setNext(constraintFileClassifier)

        return tableFileClassifier
