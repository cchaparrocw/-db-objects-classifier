# coding=utf-8
from core.classifier.FileClassifier import FileClassifier
from core.validator.FileValidators import FileValidators
import shutil

class ConstraintFileClassifier(FileClassifier):

    def __init__(self):
        FileClassifier.__init__(self)
        self.next = FileClassifier()

    def setNext(self,next):
        self.next = next

    def classifier(self,type,file,move=False):


        if type == FileValidators.CONSTRAINT_FK.value :
            path = self._router.getPath("fk",self._extractor.getModule(file))
            self.copy(file, path)
        elif type == FileValidators.CONSTRAINT_NOFK.value :
            path = self._router.getPath("nofk",self._extractor.getModule(file))
            self.copy(file, path)
        else:
            self.next.classifier(type,file,move)
