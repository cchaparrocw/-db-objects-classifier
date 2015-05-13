from core.extractor.Querys import querys

class get_index():
	query=querys()

	def get_table_indices(self,table):
		"""returm table indices"""
		rs = self.query.select_qry('querystr=self.TINDEXES_INFO_SQL',table)
		col_str=[]
		idx_lines = []

		for row in rs:
			idx_cols = []
			rs2 = self.query.select_qry('querystr=self.TINDEXES_COLUMNS_INFO_SQL',row[1])
			tmp_str=''
			for rowcolumns in rs2:
				idx_cols.append(str(rowcolumns[0])+' ASC')
			tmp_str='\n\t\t,'.join(idx_cols)
			if row[0] is None:
				type=''
			else:
				type=row[0]+' '
			idx_lines.append('CREATE %sINDEX %s ON %s \n\t(\n\t\t%s\n\t) TABLESPACE INDICES \n/' % (type,row[1] , table, tmp_str))

		return '\n\n'.join(idx_lines)

	def save_indexes_definition(self,table):
		"""saves DDL in a file"""
		s = self.get_table_indices(table)
		if s:
			return(s,table,'indice')
		else:
			return ''