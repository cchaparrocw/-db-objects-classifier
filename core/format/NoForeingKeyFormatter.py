# coding=utf-8
import os
import re
from core.format.FileFormatter import FileFormatter

class NoForeingKeyFormatter(FileFormatter):

	def isNotForeingKeyDirectory(self,directory):

		if 'constraint' in directory and '\\nofk' in directory :
			return True
		else:
			return False

	def setNext(self,next):
		self.next = next


	def tabular(self,cadena, constraint):
		posicionForeing = cadena.rfind("ADD")
		tabulacion = cadena[:posicionForeing] + "\n\t"+cadena[posicionForeing:]
		cadena = tabulacion

		posicionReferences = cadena.rfind( constraint )
		tabulacion = cadena[:posicionReferences] + " \n\t\t" + cadena[posicionReferences:]
		posicionPuntoComa = tabulacion.rfind(";")
		tabulacion = tabulacion[:posicionPuntoComa]

		return tabulacion

	def tabularPrimary(self,cadena):
		return self.tabular(cadena,"PRIMARY")

	def tabularUnique(self,cadena):
		return self.tabular(cadena,"UNIQUE")

	def tabularCheck(self,cadena):
		return self.tabular(cadena,"CHECK")

	def tabularConstraint(self,cadena):
		if "PRIMARY" in cadena:
			return self.tabularPrimary(cadena)
		elif "UNIQUE" in cadena:
			return self.tabularUnique(cadena)
		elif "CHECK" in cadena:
			return self.tabularCheck(cadena)
		else:
			return  cadena


	def format(self, directory):
    	#afterline almacena el nombre del archivo anterior
    	#si son iguales se unen ambos archivos

		if self.isNotForeingKeyDirectory(directory):
			pattern = '(_c[0-9]*|_pk|_u[0-9]*)\.sql$'
			grupos = self.agrupar(directory,pattern)
			grupos = filter(None,grupos)
			for grupo in grupos:
				concat = ""
				nombre = ""
				for archivo in grupo:
					cadena = open( directory +"\\"+ archivo).read()
					#if not "MODIFY" in cadena:

					concat = cadena.replace("\"", "")
					#concat += self.tabularConstraint(cadena)
					#concat +="\n/ \n\n"
				 	nombre = str(archivo)[:str(archivo).rfind("_")] + ".sql"

				with open( directory  +"\\"+ nombre,"a+") as f:
					f.write(concat)

			for grupo in grupos:
				for archivo in grupo:
					os.remove( directory +"\\"+archivo )
		else:
			self.next.format(directory)
