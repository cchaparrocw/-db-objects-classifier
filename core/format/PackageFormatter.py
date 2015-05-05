# coding=utf-8
import os
import re
import shutil
from core.format.FileFormatter import FileFormatter
from core.ModuleExtractor import ModuleExtractor

class PackageFormatter(FileFormatter):
    def format(self, directory):
        if self.isPackageDirectory(directory):
            for fileList in os.walk(directory):
                for files in fileList:
                    for archivo in files:
                        print(archivo)
                        if( len(archivo)>2 ):
                            extractor = ModuleExtractor()
                            module = extractor.getModule(archivo)
                            path = directory+"\\"+module+"\\"+archivo
                            self.removeFirstLine( path )
                            #self.renameFile(path)
		else:
			self.next.format(directory)
    def removeFirstLine(self,archivo):
        print("entra a quitar laprimera linea" + archivo)
        lines = open(archivo).readlines()
        lines = lines[1:]
        file = open(archivo, 'w')
        for line in lines:
            file.write(line)
        file.close()

    def renameFile(self,archivo):
        #revisa si es la definicion del paquete
        if "pks" in archivo:
            renameFile = archivo[:archivo.rfind("pks")] + "sql"
        #revisa si es el cuerpo del paqute.
        if "pkb" in archivo:
            renameFile = archivo[:archivo.rfind("pkb")] + "sql"
        os.rename(archivo,renameFile)
    def setNext(self,next):
        self.next = next


    def isPackageDirectory(self,directory):
		if '\\p' in directory :
			return True
		else:
			return False
