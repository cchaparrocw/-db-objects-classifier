# coding=utf-8
from core.classifier.FileClassifier import FileClassifier
from  core.validator.FileValidators import FileValidators
import shutil

class TableFileClassifier(FileClassifier):

    def __init__(self):
        FileClassifier.__init__(self)
        self.next = FileClassifier()

    def setNext(self,next):
        self.next = next

    def classifier(self,tipo,file,move=False):
        if tipo == FileValidators.TABLE.value :
            module = self._extractor.getModule(file)
            path = self._router.getPath("table",module)
            self.copy(file, path)
        else:
            self.next.classifier(tipo,file,move)
