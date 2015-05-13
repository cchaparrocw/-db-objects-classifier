from core.extractor.Querys import querys

class get_foreign():
	query=querys()

	def get_foreign_keys_dict(self,table):
		"""returns dictionary with info about foreign keys"""
		fk = {}
		rs = self.query.select_qry('querystr=self.TFOREIGN_KEYS_INFO_SQL',table)
		for row in rs:
			_, cn1, _, tn2, _, cn2, dr, cn = row
			try:
				_ = fk[cn][0]
				_ = fk[cn][2]
			except KeyError:
				fk[cn] = [[cn1, ], [tn2, ], [cn2, ], [dr, ]]
		return fk


	def add_foreign_key_ddl(self,table):
		"""creates DDL information about foreign keys"""
		lines_ct=[]

		rs = self.query.select_qry('querystr=self.NUMBER_OF_CONSTRAINTS',table)
		contains=rs[0]

		if contains[0] > 0:
			fk = self.get_foreign_keys_dict(table)
			if fk:
				fkk = fk.keys()
				fkk.sort()
				for cn in fkk:
					columns1 = fk[cn][0]
					table2 = fk[cn][1][0]
					columns2 = fk[cn][2]
					tmp_str = 'ALTER TABLE %s\n\tADD CONSTRAINT %s FOREIGN KEY \n\t(\n\t%s\n\t)\n\t REFERENCES %s \n\t(\n\t%s\n\t)\n/' % (table,cn, ','.join(columns1), table2, ','.join(columns2))
					lines_ct.append(tmp_str)
		return '%s' % ('\n\n'.join(lines_ct))
		
	def save_foreign_key_definition(self,table):
		"""saves DDL in a file"""
		s = self.add_foreign_key_ddl(table)
		if s:
			return(s,table,'fk')
		else:
			 return ('',table,'fk')
