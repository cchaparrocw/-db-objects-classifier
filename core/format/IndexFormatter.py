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
			pattern = '((_[a-zA-Z]([0-9]*)|pk)index\.(sql|SQL)$)'
			grupos = self.agrupar(directory,pattern)
			grupos = filter(None,grupos)

			for grupo in grupos:
				concat = ""
				nombre = ""
				print("--- grupo ----")
				print(str(grupo))

				for archivo in grupo:
					concat += open( directory +"\\"+ archivo).read()
					#if not "MODIFY" in cadena:

					#concat = cadena.replace("\"", "")
					#concat += self.tabularConstraint(cadena)
					#concat +="\n/ \n\n"
				 	nombre = str(archivo)[:str(archivo).rfind("_")] + ".sql"

				with open( directory  +"\\"+ nombre,"a+") as f:
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
