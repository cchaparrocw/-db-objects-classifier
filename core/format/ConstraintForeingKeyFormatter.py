# coding=utf-8
import os
import re
class ConstraintForeingKeyFormatter:

	def isForeingKeyDirectory(self,directory):
		if 'constraint' in directory and 'fk'in directory :
			return True
		else:
			return False 

	def format(self, directory):
    	#afterline almacena el nombre del archivo anterior
    	#si son iguales se unen ambos archivos

		AfterFile=''

		if self.isForeingKeyDirectory(directory):
			for fileList in os.walk(directory):
				for files in fileList:
					#for archivo in files:
					print([m.group(1) for l in files for m in [re.search(l,files)] if m])
					#src=regex.search; 
					#lst=[m.group(1) for l in lines for m in [src(l)] if m]
						#print( "----------------------\n")
						#print( str(archivo)[:str(archivo).rfind("_")])
						#print( "----------------------\n")
						#print(str(fname).split("_"))
