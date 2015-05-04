# coding=utf-8
import os
import re
from core.format.FileFormatter import FileFormatter

class ConstraintForeingKeyFormatter(FileFormatter):

	def __init__(self):
		self.next = FileFormatter()

	def isForeingKeyDirectory(self,directory):
		if 'constraint' in directory and '\\fk' in directory :
			return True
		else:
			return False

	def setNext(self,next):
		self.next = next

	def tabular(self,cadena):
		posicionForeing = cadena.rfind("FOREIGN")
		tabulacion = cadena[:posicionForeing] + "\n\t"+cadena[posicionForeing:]
		cadena = tabulacion

		posicionReferences = cadena.rfind("REFERENCES")
		tabulacion = cadena[:posicionReferences] + " \n\t\t" + cadena[posicionReferences:]
		posicionPuntoComa = tabulacion.rfind(";")
		tabulacion = tabulacion[:posicionPuntoComa]

		return tabulacion

	def format(self, directory):
    	#afterline almacena el nombre del archivo anterior
    	#si son iguales se unen ambos archivos
		#print(directory)
		if self.isForeingKeyDirectory(directory):
			grupos = self.agrupar(directory)
			grupos = filter(None,grupos)
			for grupo in grupos:
				concat = ""
				nombre = ""
				for archivo in grupo:
					cadena = open( directory +"\\"+ archivo).read()
					concat += self.tabular(cadena)
					concat +="\n/ \n\n"
				 	nombre = str(archivo)[:str(archivo).rfind("_")] + ".sql"

				with open( directory  +"\\"+ nombre,"a+") as f:
					f.write(concat)

			for grupo in grupos:
				for archivo in grupo:
					os.remove( directory +"\\"+archivo )
		else:
			self.next.format(directory)
