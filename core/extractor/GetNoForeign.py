from core.extractor.Querys import querys

class get_no_foreign():
	query=querys()

	def add_noforeign_key_ddl(self,table):
		"""adds information about primary key columns"""
		rs = self.query.select_qry('querystr=self.NO_FOREIGN_KEYS_INFO_SQL',table)
		nfk_columns = []
		for row in rs:
			if row[2]=='P':
				tmp_str = 'ALTER TABLE %s \n\t ADD CONSTRAINT %s PRIMARY KEY (%s) \n/' % (row[0],row[1],row[3])
				nfk_columns.append(tmp_str)
			if row[2]=='U':
				tmp_str = 'ALTER TABLE %s \n\t ADD CONSTRAINT %s UNIQUE (%s) \n/' % (row[0],row[1],row[3])
				nfk_columns.append(tmp_str)
			if row[2]=='C':
				tmp_str = 'ALTER TABLE %s \n\t ADD CONSTRAINT %s \n CHECK (%s) \n/' % (row[0],row[1],row[4])
				nfk_columns.append(tmp_str)
		return '%s' % ('\n\n'.join(nfk_columns))

	def save__noforeign_key_definition(self,table):
		"""saves DDL in a file"""
		s = self.add_noforeign_key_ddl(table)
		if s:
			return(s,table,'nofk')
		else:
			return ('',table,'nofk')