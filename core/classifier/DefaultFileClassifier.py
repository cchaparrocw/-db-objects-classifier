# coding=utf-8
from core.classifier.FileClassifier import FileClassifier
from  core.validator.FileValidators import FileValidators
import shutil

class DefaultFileClassifier(FileClassifier):

    def __init__(self):
        FileClassifier.__init__(self)
        self.next = FileClassifier()

    def setNext(self,next):
        self.next = next

    def classifier(self,type,file):
        path = self._router.getPath("default","")
        self.copy(file, path)
