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

    def classifier(self,type,file):
        if type == FileValidators.TABLE.value :
            shutil.move(file, "build/sql/fisica/table")
        else:
            self.next.classifier(type,file)
