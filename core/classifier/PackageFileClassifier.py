
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
        if type == FileValidators.PACKAGE.value :
            shutil.copy2(file, "build/sql/fisica/logica-plsql/package")
        elif type == FileValidators.PACKAGE_BODY.value:
            shutil.copy2(file, "build/sql/fisica/logica-plsql/package-body")
        else:
            self.next.classifier(type,file)
