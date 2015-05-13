# coding=utf-8

from core.extractor.Querys import querys

class get_tables():

	def format_columns(self,text,length):
		space=length-len(text) 
		tmp_str=text+" "*space
		#print (text+' ' + str(space)+' ' + str(len(tmp_str)))
		#raw_input("Pulsa una tecla para continuar...") 
		return tmp_str

	def get_type_length(self,data_type, data_length, char_length):
		"""get string with length of field"""
		if data_type == 'NUMBER':
			if data_length == ',':
				return ''
			if data_length == ',0':
				return '(*,0)'
			return '(%s)' % (data_length)
		if data_type == 'RAW':
			return ' (%s)' % (data_length)
		if data_type in ('CHAR', 'VARCHAR2', 'NCHAR', 'NVARCHAR2'):
			return ' (%.0f)' % (char_length)
		return ''

	def get_table_comments(self,table):
		"""returm table comments"""
		query=querys()
		max_length=0
		rs = query.select_qry('querystr=self.TABLE_COMMENTS_SQL', table)
		comments = []

		
		# trace for the word more large into vector
		for row in rs:
			if len(row[0]) > max_length:
				max_length = len(row[0])

		# agregate spaces into the other lines of vector
		for row in rs:

			tmp_str = 'COMMENT ON COLUMN %s IS \'%s\' ;' % (self.format_columns(row[0],max_length),row[1])
			comments.append(tmp_str)
		return '\n'.join(comments)
	
	def table_info_row(self,row):
		"""shows info about table column"""
		column_name = row[0]
		data_type = row[1]
		nullable = row[2]
		hasdef = row[3]
		data_length = row[4]
		data_default = row[5]
		char_length = row[6]
		default_str = nullable_str = ''
		data_length_str = self.get_type_length(data_type, data_length, char_length)
		if int(hasdef) == 1:
			default_str = ' DEFAULT %s' % (data_default)
		if nullable == 'N':
			nullable_str = ' NOT NULL'
			if default_str.endswith(' '):
				nullable_str = 'NOT NULL'
		if column_name.startswith('_'):
			column_name = '"' + column_name + '"'
		else:
			pass#column_name = column_name.lower()
		return '%(column_name)s %(data_type)s%(data_length)s%(default)s%(nullable)s' % {'column_name': column_name, 'data_type': data_type, 'data_length': data_length_str, 'nullable': nullable_str, 'default': default_str}


	def create_create_table_ddl(self,table):
		"""creates DDL with CREATE TABLE for table"""
		# gets information about columns
		query=querys()
		rs = query.select_qry('querystr=self.TTABLE_COLUMNS_SQL' ,table)
		lines_ct = []
		lines_sc = []
		table_comments = []
		containLOB=False;
		campLOB=[];
		containXML=False;
		campXML=[];
		count_lob=1;
		for row in rs:
			columnsplit=self.table_info_row(row).strip()
			lines_ct.append(columnsplit)
			
			if 'LOB' in row[1]:
				containLOB=True
				campLOB.append(row[0])
			if 'XML' in row[1]:
				containXML=True
				campXML.append(row[0])

		ct = 'CREATE TABLE %s (\n\t %s\n)TABLESPACE DATOS \n' % (table, '\n\t,'.join(lines_ct))

		if containXML:
			for x in campXML:
				ct = ct + 'XMLTYPE  COLUMN %s STORE AS CLOB ( \n    TABLESPACE BINARIOS \n    INDEX %s ( \n      TABLESPACE BINARIOS\n    )\n)\n'	%(x,table+'_L'+str(count_lob))
				count_lob+=1
		if containLOB:
			for x in campLOB:
				ct = ct + 'LOB (%s) STORE AS ( \n    TABLESPACE BINARIOS \n    INDEX %s ( \n      TABLESPACE BINARIOS\n    )\n)\n'	%(x,table+'_L'+str(count_lob))
				count_lob+=1
		
		tab_comments = query.select_qry( 'querystr=self.TAB_COMMENTS_SQL',table)
		
		for row in tab_comments:
			tmp_str = 'COMMENT ON TABLE %s\t IS \'%s\' ;' % (row[0],row[2])
			table_comments.append(tmp_str)

		col_comments_str=self.get_table_comments(table)

		return '%s\n/\n%s\n\n%s' % (ct,'\n'.join(table_comments),col_comments_str)


	def save_table_definition(self,table):
		"""saves DDL in a file"""
		s = self.create_create_table_ddl(table)
		return (s,table,'table')
