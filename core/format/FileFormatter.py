# coding=utf-8
import re
class FileFormatter :
	def format(self):
		raise NotImplementedError('subclasses must override format!')
	def checkExpression( self,expression,value):
		value = value.upper()
		result = re.match( expression,value,re.IGNORECASE)
		return True if result else False
