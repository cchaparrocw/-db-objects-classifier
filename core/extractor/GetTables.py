# coding=utf-8
import get_files
import querys
class get_tables:

	def create_create_table_ddl(self,table):
	"""creates DDL with CREATE TABLE for table"""
	# gets information about columns
	rs = select_qry(TTABLE_COLUMNS_SQL % (table))
	lines_ct = []
	lines_sc = []
	table_comments = []
	containLOB=False;
	campLOB=[];
	containXML=False;
	campXML=[];
	count_lob=1;

	for row in rs:

		columnsplit=table_info_row(row).strip()
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
	
	tab_comments = select_qry( """SELECT  * 
		FROM user_tab_comments
		WHERE table_name='%s'""" % (table))
	
	for row in tab_comments:
		tmp_str = 'COMMENT ON TABLE %s\t IS \'%s\' ;' % (row[0],row[2])
		table_comments.append(tmp_str)

	col_comments_str=get_table_comments(table)
	return '%s\n/\n%s\n\n%s' % (ct,'\n'.join(table_comments),col_comments_str)


def save_table_definition(self,table):
	"""saves DDL in a file"""
	s = create_create_table_ddl(table)
	return 1
