from core.extractor.Querys import querys

class get_package():
	query=querys()

	def add_package_string(self,package):
		"""shows SQL packages"""
		package_string=[]
		package=package+'\', \'PACKAGE'
		pckg=self.query.select_qry('querystr=self.GET_PACKAGE_DEFINITION_SQL',(package))
		for x in pckg:
			package_string.append(x[0])
		tmp_string= ''.join(package_string)
		tmp_string='CREATE OR REPLACE '+ tmp_string
		return tmp_string

	def add_package_body_string(self,package):
		"""shows SQL packages"""
		package_string=[]
		package=package+'\', \'PACKAGE BODY'
		pckg=self.query.select_qry('querystr=self.GET_PACKAGE_DEFINITION_SQL',package)
		for x in pckg:
			package_string.append(x[0])
		if package_string:
			tmp_string= ''.join(package_string)
			tmp_string='CREATE OR REPLACE '+ tmp_string
			return tmp_string
		else:
			return None

	def save_package_definition(self,package):
		"""saves DDL in a file"""
		s = self.add_package_string(package)
		return(s,package,'package')

	def save_package_body_definition(self,package):
		"""saves DDL in a file"""
		s = self.add_package_body_string(package)
		if s is not None:
			return(s,package,'package_body')
		else:
			return None