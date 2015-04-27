from  core.validator.FileValidators import FileValidators

from core.classifier.TableFileClassifier import TableFileClassifier
from core.classifier.SequenceFileClassifier import SequenceFileClassifier
from core.classifier.PackageFileClassifier import PackageFileClassifier

class BuilderFileClassifier():

    def build(self):
        tableFileClassifier = TableFileClassifier()
        sequenceFileClassifier = SequenceFileClassifier()
        tableFileClassifier.setNext(sequenceFileClassifier)

        packageFileClassifier = PackageFileClassifier()
        packageFileClassifier.setNext(sequenceFileClassifier)

        return tableFileClassifier
