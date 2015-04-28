# coding=utf-8
from core.classifier.FileClassifier import FileClassifier
from  core.validator.FileValidators import FileValidators
import shutil

class ConstrainFileClassifier(FileClassifier):

    def __init__(self):
        FileClassifier.__init__(self)
        self.next = FileClassifier()

    def setNext(self,next):
        self.next = next

    def classifier(self,type,file):


        if type == FileValidators.CONSTRAINT_FK.value :
            path = self._router.getPath("fk",module)
            shutil.copy2(file, path)
        elif type == FileValidators.CONSTRAINT_NOFK.value :
            path = self._router.getPath("nofk",module)
            shutil.copy2(file, path)
        else:
            self.next.classifier(type,file)
