# coding=utf-8
import os
import re
import shutil
from core.format.FileFormatter import FileFormatter
from core.ModuleExtractor import ModuleExtractor

class ViewFormatter(FileFormatter):

    def format(self, directory):

        if self.isViewDirectory(directory):
            #para obtener solo los archivos en el directorio 
            fileList = next(os.walk(directory))[2]
            for archivo in fileList:
                if( len(archivo)>2 ):
                    path = directory+"\\"+archivo
                    self.renameFile(path)
        else:
			self.next.format(directory)

    def renameFile(self,archivo):
        renameFile = archivo[:archivo.rfind("vw")] + "sql"
        os.rename(archivo,renameFile)
    def setNext(self,next):
        self.next = next


    def isViewDirectory(self,directory):
		if '\\datos' in directory :
			return True
		else:
			return False
