# coding=utf-8
from core.classifier.FileClassifier import FileClassifier
from  core.validator.FileValidators import FileValidators
import shutil

class ViewFileClassifier(FileClassifier):

    def __init__(self):
        FileClassifier.__init__(self)
        self.next = FileClassifier()

    def setNext(self,next):
        self.next = next


    def classifier(self,type,file):
        if type == FileValidators.VIEW_BI.value :
            shutil.copy2(file, "build/sql/query/bi")
        elif type == FileValidators.VIEW_DATA.value :
                shutil.copy2(file, "build/sql/query/datos")
            elif type == FileValidators.VIEW_JOIN.value :
                    shutil.copy2(file, "build/sql/query/join")
                elif type == FileValidators.VIEW_LOV.value :
                    shutil.copy2(file, "build/sql/query/lov")
                    elif type == FileValidators.VIEW_REPORT.value :
                    shutil.copy2(file, "build/sql/query/report")
                    else :
                        self.next.classifier(type,file)