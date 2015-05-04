# coding=utf-8
import re
import os
class FileFormatter :
	def format(self):
		raise NotImplementedError('subclasses must override format!')

	def setNext(self):
		raise NotImplementedError('subclasses must override setNext!')

	def checkExpression( self,expression,value):
		value = value.upper()
		result = re.match( expression,value,re.IGNORECASE)
		return True if result else False
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
						#modificar el patron para que sea definido por parametro y funcione para los demas formatos
						pattern = "("+principal+")_(F[0-9]*)\.sql"
						#print(pattern)
						if self.checkExpression(pattern,archivo ):
							grupo.append( archivo )
					grupos.append(grupo)
		return grupos
