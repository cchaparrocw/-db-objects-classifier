# coding=utf-8
import os
import re
from core.format.FileFormatter import FileFormatter

class ConstraintForeingKeyFormatter(FileFormatter):

	def isForeingKeyDirectory(self,directory):
		if 'constraint' in directory and 'fk'in directory :
			return True
		else:
			return False

	def agrupar(self,directory):
		archivos = []
		for fileList in os.walk(directory):
			for files in fileList:
				for archivo in files:
					archivos.append( str(archivo)[:str(archivo).rfind("_")])

		archivos = list(set(archivos))
		archivos = filter(None,archivos)
		grupos = []
		#se agrupan los archivos
		for principal in archivos:
			for fileList in os.walk(directory):
				for files in fileList:
					grupo = []
					for archivo in files:
						pattern = "("+principal+")_(F[0-9]*)\.sql"
						#print(pattern)
						if self.checkExpression(pattern,archivo ):
							grupo.append( archivo )
					grupos.append(grupo)
		return grupos

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
