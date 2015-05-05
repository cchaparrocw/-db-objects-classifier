# coding=utf-8
import os
import re
import shutil
from core.format.FileFormatter import FileFormatter
from core.ModuleExtractor import ModuleExtractor

class IndexFormatter(FileFormatter):

	def isIndexDirectory(self,directory):
		if '\\indice' in directory :
			return True
		else:
			return False

	def setNext(self,next):
		self.next = next

	def format(self, directory):
		if self.isIndexDirectory(directory):
			pattern = '(_I[0-9]*)\.sql$'
			grupos = self.agrupar(directory,pattern)
			grupos = filter(None,grupos)
			for grupo in grupos:
				concat = ""
				nombre = ""
				print("--- grupo ----")
				for archivo in grupo:

					if "_I" in archivo  and ".sql" in archivo:
						extractor = ModuleExtractor()
						module = extractor.getModule(archivo)
						path = directory+"\\"+module+"\\"+archivo
						print(path)
						concat = open( path ).read()
						concat +="\n/ \n\n"
					 	nombre = str(archivo)[:str(archivo).rfind("_")] + ".sql"
						print(nombre)
					with open(  directory+"\\"+module+"\\"+ nombre,"a+") as f:
						f.write(concat)

				print("---fin---")
			for grupo in grupos:
				for archivo in grupo:
					extractor = ModuleExtractor()
					module = extractor.getModule(archivo)
					path = directory+"\\"+module+"\\"+archivo
					os.remove( path )


		else:
			self.next.format(directory)
