
# coding=utf-8
from core.classifier.FileClassifier import FileClassifier
from  core.validator.FileValidators import FileValidators
import shutil

class PackageFileClassifier(FileClassifier):

    def __init__(self):
        FileClassifier.__init__(self)
        self.next = FileClassifier()

    def setNext(self,next):
        self.next = next

    def classifier(self,type,file):
        module = self._extractor.getModule(file)
        if type == FileValidators.PACKAGE.value :
            path = self._router.getPath("package",module)
            self.copy(file, path)
        elif type == FileValidators.PACKAGE_BODY.value:
            path = self._router.getPath("package_body",module)
            self.copy(file, path)
        else:
            self.next.classifier(type,file)
