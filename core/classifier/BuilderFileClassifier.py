from  core.validator.FileValidators import FileValidators

from core.classifier.TableFileClassifier import TableFileClassifier
from core.classifier.SequenceFileClassifier import SequenceFileClassifier
from core.classifier.PackageFileClassifier import PackageFileClassifier
from core.classifier.ViewFileClassifier import ViewFileClassifier
from core.classifier.ConstraintFileClassifier import ConstraintFileClassifier
from core.classifier.DefaultFileClassifier import DefaultFileClassifier
from core.classifier.IndexFileClassifier import IndexFileClassifier

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

        indexFileClassifier = IndexFileClassifier()
        constraintFileClassifier.setNext(indexFileClassifier)

        defaultFileClassifier = DefaultFileClassifier() 
        indexFileClassifier.setNext(defaultFileClassifier)

        return tableFileClassifier
