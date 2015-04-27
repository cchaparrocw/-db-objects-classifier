from  core.validator.FileValidators import FileValidators

from core.classifier.TableFileClassifier import TableFileClassifier
from core.classifier.SequenceFileClassifier import SequenceFileClassifier


class BuilderFileClassifier():

    def build(self):
        tableFileClassifier = TableFileClassifier()
        sequenceFileClassifier = SequenceFileClassifier()
        tableFileClassifier.setNext(sequenceFileClassifier)

        return tableFileClassifier
