# coding=utf-8
from core.classifier.FileClassifier import FileClassifier
from  core.validator.FileValidators import FileValidators
import shutil

class IndexFileClassifier(FileClassifier):

    def __init__(self):
        FileClassifier.__init__(self)
        self.next = FileClassifier()

    def setNext(self,next):
        self.next = next

    def classifier(self,type,file):
        if type == FileValidators.INDEX.value :
            print(file)
            print( "es indice" )
            module = self._extractor.getModule(file)
            print(module)
            path = self._router.getPath("indice",module)
            print(path)
            self.copy(file, path)
        else:
            self.next.classifier(type,file)
