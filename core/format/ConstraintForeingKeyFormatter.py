# coding=utf-8
import os
class ConstraintForeingKeyFormatter:

	def isForeingKeyDirectory(self,directory):
		if 'constraint' in directory and 'nofk'in directory :
			return True
		else:
			return False 

	def format(self, directory):
    	#afterline almacena el nombre del archivo anterior
    	#si son iguales se unen ambos archivos
		AfterFile=''
		if self.isForeingKeyDirectory(directory):
			for fileList in os.walk(directory):
				for fname in fileList:
					print(fname.split("_"))
